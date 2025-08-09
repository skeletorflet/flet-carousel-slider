import 'package:flet/flet.dart';

import 'flet_carousel_slider.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "flet_carousel_slider":
      return FletCarouselSliderControl(
        parent: args.parent,
        control: args.control,
        children: args.children,
        parentDisabled: args.parentDisabled,
        parentAdaptive: args.parentAdaptive,
        backend: args.backend,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
