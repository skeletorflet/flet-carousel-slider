import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:carousel_slider/carousel_slider.dart';
import 'dart:convert';

class FletCarouselSliderControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final List<Control> children;
  final bool parentDisabled;
  final bool? parentAdaptive;
  final FletControlBackend backend;

  const FletCarouselSliderControl({
    super.key,
    required this.parent,
    required this.control,
    required this.children,
    required this.parentDisabled,
    required this.parentAdaptive,
    required this.backend,
  });

  @override
  State<FletCarouselSliderControl> createState() =>
      _FletCarouselSliderControlState();
}

class _FletCarouselSliderControlState extends State<FletCarouselSliderControl> {
  late CarouselSliderController _carouselController;
  int _currentPage = 0;
  bool _autoPlay = false;

  @override
  void initState() {
    super.initState();
    _carouselController = CarouselSliderController();
    widget.backend.subscribeMethods(widget.control.id, _onMethodCall);
    _currentPage = widget.control.attrInt("initialPage", 0) ?? 0;
    _autoPlay = widget.control.attrBool("autoPlay", false) ?? false;
  }

  @override
  void dispose() {
    widget.backend.unsubscribeMethods(widget.control.id);
    super.dispose();
  }

  Future<String?> _onMethodCall(
      String methodName, Map<String, String> args) async {
    switch (methodName) {
      case "next_page":
        final int duration = int.tryParse(args["duration"] ?? "300") ?? 300;
        final String curve = args["curve"] ?? "linear";
        _carouselController.nextPage(
          duration: Duration(milliseconds: duration),
          curve: parseCurve(curve, Curves.linear)!,
        );
        return null;

      case "previous_page":
        final int duration = int.tryParse(args["duration"] ?? "300") ?? 300;
        final String curve = args["curve"] ?? "linear";
        _carouselController.previousPage(
          duration: Duration(milliseconds: duration),
          curve: parseCurve(curve, Curves.linear)!,
        );
        return null;

      case "jump_to_page":
        final int page = int.tryParse(args["page"] ?? "0") ?? 0;
        _carouselController.jumpToPage(page);
        return null;

      case "animate_to_page":
        final int page = int.tryParse(args["page"] ?? "0") ?? 0;
        final int duration = int.tryParse(args["duration"] ?? "300") ?? 300;
        final String curve = args["curve"] ?? "linear";
        _carouselController.animateToPage(
          page,
          duration: Duration(milliseconds: duration),
          curve: parseCurve(curve, Curves.linear)!,
        );
        return null;

      case "get_current_page":
        return _currentPage.toString();

      case "start_auto_play":
        setState(() {
          _autoPlay = true;
          // Update control state so Python side reflects the change
          widget.backend
              .updateControlState(widget.control.id, {"autoPlay": "true"});
        });
        return null;

      case "stop_auto_play":
        setState(() {
          _autoPlay = false;
          widget.backend
              .updateControlState(widget.control.id, {"autoPlay": "false"});
        });
        return null;

      default:
        return null;
    }
  }

  CenterPageEnlargeStrategy _getEnlargeStrategy(String? strategy) {
    switch (strategy?.toLowerCase()) {
      case "scale":
        return CenterPageEnlargeStrategy.scale;
      case "height":
        return CenterPageEnlargeStrategy.height;
      case "zoom":
        return CenterPageEnlargeStrategy.zoom;
      default:
        return CenterPageEnlargeStrategy.scale;
    }
  }

  Axis _getScrollDirection(String? direction) {
    switch (direction?.toLowerCase()) {
      case "vertical":
        return Axis.vertical;
      case "horizontal":
      default:
        return Axis.horizontal;
    }
  }

  void _onPageChanged(int index, CarouselPageChangedReason reason) {
    setState(() {
      _currentPage = index;
    });

    // Trigger page changed event
    final eventData = {
      "index": index,
      "reason": reason.toString().split('.').last,
    };

    widget.backend.triggerControlEvent(
      widget.control.id,
      "page_changed",
      json.encode(eventData),
    );
  }

  void _onScrolled(double? position) {
    if (position == null) return;

    // Normalize the offset to be more user-friendly
    // CarouselSlider internally uses large numbers, let's make it relative to current page
    final itemCount = widget.children
        .where((c) => c.name?.startsWith("item_") == true && c.isVisible)
        .length;
    double normalizedOffset = _currentPage.toDouble();

    if (itemCount > 0) {
      // Calculate fractional part based on position relative to a reasonable base
      double fractionalPart =
          (position % 100) / 100; // Use mod 100 to get a 0-1 range
      normalizedOffset = _currentPage + fractionalPart;

      // Keep it within bounds
      if (normalizedOffset < 0) normalizedOffset = 0;
      if (normalizedOffset >= itemCount)
        normalizedOffset = itemCount - 1 + fractionalPart;
    }

    final eventData = {
      "offset": double.parse(
          normalizedOffset.toStringAsFixed(2)), // Round to 2 decimals
      "current_page": _currentPage,
      "raw_offset": position, // Keep raw for debugging if needed
    };

    widget.backend.triggerControlEvent(
      widget.control.id,
      "scrolled",
      json.encode(eventData),
    );
  }

  @override
  Widget build(BuildContext context) {
    // Get carousel items from children
    final itemControls = widget.children
        .where((c) => c.name?.startsWith("item_") == true && c.isVisible);

    bool disabled = widget.control.isDisabled || widget.parentDisabled;
    bool? adaptive =
        widget.control.attrBool("adaptive") ?? widget.parentAdaptive;

    // Build carousel items
    List<Widget> carouselItems = itemControls.map((itemControl) {
      return createControl(
        widget.control,
        itemControl.id,
        disabled,
        parentAdaptive: adaptive,
      );
    }).toList();

    // If no items provided, show placeholder
    if (carouselItems.isEmpty) {
      carouselItems = [
        Container(
          child: const Center(
            child: Text(
              "No items provided",
              style: TextStyle(fontSize: 16, color: Colors.grey),
            ),
          ),
        ),
      ];
    }

    // Parse carousel options
    final double? height = widget.control.attrDouble("height");
    final double aspectRatio =
        widget.control.attrDouble("aspectRatio", 16 / 9) ?? 16 / 9;
    final double viewportFraction =
        widget.control.attrDouble("viewportFraction", 0.8) ?? 0.8;
    final int initialPage = widget.control.attrInt("initialPage", 0) ?? 0;
    final bool enableInfiniteScroll =
        widget.control.attrBool("enableInfiniteScroll", true) ?? true;
    final bool animateToClosest =
        widget.control.attrBool("animateToClosest", true) ?? true;
    final bool reverse = widget.control.attrBool("reverse", false) ?? false;
    // Use internal _autoPlay flag if method calls changed it during runtime
    final bool autoPlay = _autoPlay;
    final int autoPlayInterval =
        widget.control.attrInt("autoPlayInterval", 4000) ?? 4000;
    final int autoPlayAnimationDuration =
        widget.control.attrInt("autoPlayAnimationDuration", 800) ?? 800;
    final String autoPlayCurve =
        widget.control.attrString("autoPlayCurve", "fastOutSlowIn") ??
            "fastOutSlowIn";
    final bool enlargeCenterPage =
        widget.control.attrBool("enlargeCenterPage", false) ?? false;
    final double enlargeFactor =
        widget.control.attrDouble("enlargeFactor", 0.3) ?? 0.3;
    final String enlargeStrategy =
        widget.control.attrString("enlargeStrategy", "scale") ?? "scale";
    final bool pageSnapping =
        widget.control.attrBool("pageSnapping", true) ?? true;
    final String scrollDirection =
        widget.control.attrString("scrollDirection", "horizontal") ??
            "horizontal";
    final bool pauseAutoPlayOnTouch =
        widget.control.attrBool("pauseAutoPlayOnTouch", true) ?? true;
    final bool pauseAutoPlayOnManualNavigate =
        widget.control.attrBool("pauseAutoPlayOnManualNavigate", true) ?? true;
    final bool pauseAutoPlayInFiniteScroll =
        widget.control.attrBool("pauseAutoPlayInFiniteScroll", false) ?? false;
    final bool disableCenter =
        widget.control.attrBool("disableCenter", false) ?? false;
    final bool padEnds = widget.control.attrBool("padEnds", true) ?? true;

    // Check if user wants scroll events (to avoid spam)
    final bool enableScrollEvents =
        widget.control.attrBool("enableScrollEvents", false) ?? false;

    // Configure scroll physics for vertical carousels to prevent conflicts
    ScrollPhysics? scrollPhysics;
    if (_getScrollDirection(scrollDirection) == Axis.vertical) {
      // Use ClampingScrollPhysics for vertical carousels to prevent bounce conflicts
      scrollPhysics = const ClampingScrollPhysics();
    }

    // Create CarouselOptions
    final CarouselOptions options = CarouselOptions(
      height: height,
      aspectRatio: aspectRatio,
      viewportFraction: viewportFraction,
      initialPage: initialPage,
      enableInfiniteScroll: enableInfiniteScroll,
      animateToClosest: animateToClosest,
      reverse: reverse,
      autoPlay: autoPlay,
      autoPlayInterval: Duration(milliseconds: autoPlayInterval),
      autoPlayAnimationDuration:
          Duration(milliseconds: autoPlayAnimationDuration),
      autoPlayCurve: parseCurve(autoPlayCurve, Curves.fastOutSlowIn)!,
      enlargeCenterPage: enlargeCenterPage,
      enlargeFactor: enlargeFactor,
      enlargeStrategy: _getEnlargeStrategy(enlargeStrategy),
      pageSnapping: pageSnapping,
      scrollDirection: _getScrollDirection(scrollDirection),
      scrollPhysics: scrollPhysics,
      pauseAutoPlayOnTouch: pauseAutoPlayOnTouch,
      pauseAutoPlayOnManualNavigate: pauseAutoPlayOnManualNavigate,
      pauseAutoPlayInFiniteScroll: pauseAutoPlayInFiniteScroll,
      disableCenter: disableCenter,
      padEnds: padEnds,
      onPageChanged: _onPageChanged,
      onScrolled: enableScrollEvents ? _onScrolled : null,
    );

    // Create the CarouselSlider widget
    Widget carouselSlider = CarouselSlider(
      items: carouselItems,
      carouselController: _carouselController,
      options: options,
    );

    // For vertical carousels, wrap with Listener to handle mouse wheel better
    if (_getScrollDirection(scrollDirection) == Axis.vertical) {
      carouselSlider = Listener(
        onPointerSignal: (pointerSignal) {
          if (pointerSignal is PointerScrollEvent) {
            // Handle mouse wheel for vertical carousel
            if (pointerSignal.scrollDelta.dy > 0) {
              // Scroll down -> next page
              _carouselController.nextPage(
                duration: const Duration(milliseconds: 300),
                curve: Curves.easeInOut,
              );
            } else if (pointerSignal.scrollDelta.dy < 0) {
              // Scroll up -> previous page
              _carouselController.previousPage(
                duration: const Duration(milliseconds: 300),
                curve: Curves.easeInOut,
              );
            }
          }
        },
        child: carouselSlider,
      );
    }

    return constrainedControl(
      context,
      carouselSlider,
      widget.parent,
      widget.control,
    );
  }
}
