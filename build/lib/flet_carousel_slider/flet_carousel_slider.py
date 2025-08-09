from enum import Enum
from typing import Any, Optional, List, Union
import json
import uuid

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber, Control
from flet.core.types import (
    OptionalControlEventCallable,
)
from flet.core.animation import AnimationCurve

class CarouselPageChangedReason(Enum):
    """
    Enum for carousel page changed reasons.
    """
    CONTROLLER = "controller"
    MANUAL = "manual"
    TIMED = "timed"

class CenterPageEnlargeStrategy(Enum):
    """
    Enum for center page enlarge strategy.
    """
    SCALE = "scale"
    HEIGHT = "height"
    ZOOM = "zoom"

class ScrollDirection(Enum):
    """
    Enum for scroll direction.
    """
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

class FletCarouselSlider(ConstrainedControl):
    """
    A carousel slider widget for Flet that wraps Flutter's carousel_slider package.

    Features:
    - Infinite scroll
    - Custom child widgets
    - Auto play
    - Manual control with CarouselController
    - Various customization options
    """

    def __init__(
        self,
        #
        # Control
        #
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        #
        # ConstrainedControl
        #
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        #
        # FletCarouselSlider specific
        #
        items: Optional[List[Control]] = None,
        height: OptionalNumber = None,
        aspect_ratio: OptionalNumber = 16/9,
        viewport_fraction: OptionalNumber = 0.8,
        initial_page: Optional[int] = 0,
        enable_infinite_scroll: Optional[bool] = True,
        animate_to_closest: Optional[bool] = True,
        reverse: Optional[bool] = False,
        auto_play: Optional[bool] = False,
        auto_play_interval: Optional[int] = 4000,  # milliseconds
        auto_play_animation_duration: Optional[int] = 800,  # milliseconds
        auto_play_curve: Optional[str] = "fastOutSlowIn",
        enlarge_center_page: Optional[bool] = False,
        enlarge_factor: OptionalNumber = 0.3,
        enlarge_strategy: Optional[CenterPageEnlargeStrategy] = CenterPageEnlargeStrategy.SCALE,
        page_snapping: Optional[bool] = True,
        scroll_direction: Optional[ScrollDirection] = ScrollDirection.HORIZONTAL,
        pause_auto_play_on_touch: Optional[bool] = True,
        pause_auto_play_on_manual_navigate: Optional[bool] = True,
        pause_auto_play_in_finite_scroll: Optional[bool] = False,
        disable_center: Optional[bool] = False,
        pad_ends: Optional[bool] = True,
        enable_scroll_events: Optional[bool] = False,
        on_page_changed: OptionalControlEventCallable = None,
        on_scrolled: OptionalControlEventCallable = None,
    ):
        ConstrainedControl.__init__(
            self,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        self.items = items or []
        self.height = height
        self.aspect_ratio = aspect_ratio
        self.viewport_fraction = viewport_fraction
        self.initial_page = initial_page
        self.enable_infinite_scroll = enable_infinite_scroll
        self.animate_to_closest = animate_to_closest
        self.reverse = reverse
        self.auto_play = auto_play
        self.auto_play_interval = auto_play_interval
        self.auto_play_animation_duration = auto_play_animation_duration
        self.auto_play_curve = auto_play_curve
        self.enlarge_center_page = enlarge_center_page
        self.enlarge_factor = enlarge_factor
        self.enlarge_strategy = enlarge_strategy
        self.page_snapping = page_snapping
        self.scroll_direction = scroll_direction
        self.pause_auto_play_on_touch = pause_auto_play_on_touch
        self.pause_auto_play_on_manual_navigate = pause_auto_play_on_manual_navigate
        self.pause_auto_play_in_finite_scroll = pause_auto_play_in_finite_scroll
        self.disable_center = disable_center
        self.pad_ends = pad_ends
        self.enable_scroll_events = enable_scroll_events
        # Initialize handler variables
        self.__on_page_changed_handler = None
        self.__on_scrolled_handler = None

        self.on_page_changed = on_page_changed
        self.on_scrolled = on_scrolled

        # Add internal event handlers for JSON decoding
        self._add_event_handler("page_changed", self._on_page_changed_internal)
        self._add_event_handler("scrolled", self._on_scrolled_internal)

    def _get_control_name(self):
        return "flet_carousel_slider"

    def _get_children(self):
        """
        Returns the list of child controls (carousel items).
        """
        children = []
        for i, item in enumerate(self.items):
            if item is not None:
                item._set_attr_internal("n", f"item_{i}")
                children.append(item)
        return children

    # items property
    @property
    def items(self) -> List[Control]:
        """
        List of widgets to be displayed in the carousel.
        """
        return self.__items

    @items.setter
    def items(self, value: Optional[List[Control]]):
        self.__items = value or []

    # height property
    @property
    def height(self) -> OptionalNumber:
        """
        Set carousel height and overrides any existing aspect_ratio.
        """
        return self._get_attr("height")

    @height.setter
    def height(self, value: OptionalNumber):
        self._set_attr("height", value)

    # aspect_ratio property
    @property
    def aspect_ratio(self) -> OptionalNumber:
        """
        Aspect ratio is used if no height have been declared.
        Defaults to 16/9.
        """
        return self._get_attr("aspectRatio")

    @aspect_ratio.setter
    def aspect_ratio(self, value: OptionalNumber):
        self._set_attr("aspectRatio", value)

    # viewport_fraction property
    @property
    def viewport_fraction(self) -> OptionalNumber:
        """
        The fraction of the viewport that each page should occupy.
        Defaults to 0.8.
        """
        return self._get_attr("viewportFraction")

    @viewport_fraction.setter
    def viewport_fraction(self, value: OptionalNumber):
        self._set_attr("viewportFraction", value)

    # initial_page property
    @property
    def initial_page(self) -> Optional[int]:
        """
        The initial page to show when first creating the CarouselSlider.
        """
        return self._get_attr("initialPage")

    @initial_page.setter
    def initial_page(self, value: Optional[int]):
        self._set_attr("initialPage", value)

    # enable_infinite_scroll property
    @property
    def enable_infinite_scroll(self) -> Optional[bool]:
        """
        Determines if carousel should loop infinitely or be limited to item length.
        """
        return self._get_attr("enableInfiniteScroll")

    @enable_infinite_scroll.setter
    def enable_infinite_scroll(self, value: Optional[bool]):
        self._set_attr("enableInfiniteScroll", value)

    # animate_to_closest property
    @property
    def animate_to_closest(self) -> Optional[bool]:
        """
        Determines if carousel should loop to the closest occurrence of requested page.
        """
        return self._get_attr("animateToClosest")

    @animate_to_closest.setter
    def animate_to_closest(self, value: Optional[bool]):
        self._set_attr("animateToClosest", value)

    # reverse property
    @property
    def reverse(self) -> Optional[bool]:
        """
        Reverse the order of items if set to true.
        """
        return self._get_attr("reverse")

    @reverse.setter
    def reverse(self, value: Optional[bool]):
        self._set_attr("reverse", value)

    # auto_play property
    @property
    def auto_play(self) -> Optional[bool]:
        """
        Enables auto play, sliding one page at a time.
        """
        return self._get_attr("autoPlay")

    @auto_play.setter
    def auto_play(self, value: Optional[bool]):
        self._set_attr("autoPlay", value)

    # auto_play_interval property
    @property
    def auto_play_interval(self) -> Optional[int]:
        """
        Sets Duration to determine the frequency of slides when auto play is enabled.
        Value in milliseconds. Defaults to 4000ms (4 seconds).
        """
        return self._get_attr("autoPlayInterval")

    @auto_play_interval.setter
    def auto_play_interval(self, value: Optional[int]):
        self._set_attr("autoPlayInterval", value)

    # auto_play_animation_duration property
    @property
    def auto_play_animation_duration(self) -> Optional[int]:
        """
        The animation duration between two transitioning pages while in auto playback.
        Value in milliseconds. Defaults to 800ms.
        """
        return self._get_attr("autoPlayAnimationDuration")

    @auto_play_animation_duration.setter
    def auto_play_animation_duration(self, value: Optional[int]):
        self._set_attr("autoPlayAnimationDuration", value)

    # auto_play_curve property
    @property
    def auto_play_curve(self) -> Optional[str]:
        """
        Determines the animation curve physics.
        Common values: "linear", "ease", "easeIn", "easeOut", "easeInOut", "fastOutSlowIn", etc.
        """
        return self._get_attr("autoPlayCurve")

    @auto_play_curve.setter
    def auto_play_curve(self, value: Optional[str]):
        self._set_attr("autoPlayCurve", value)

    # enlarge_center_page property
    @property
    def enlarge_center_page(self) -> Optional[bool]:
        """
        Determines if current page should be larger than the side images,
        creating a feeling of depth in the carousel.
        """
        return self._get_attr("enlargeCenterPage")

    @enlarge_center_page.setter
    def enlarge_center_page(self, value: Optional[bool]):
        self._set_attr("enlargeCenterPage", value)

    # enlarge_factor property
    @property
    def enlarge_factor(self) -> OptionalNumber:
        """
        How much the pages next to the center page will be scaled down.
        If enlarge_center_page is false, this property has no effect.
        Defaults to 0.3.
        """
        return self._get_attr("enlargeFactor")

    @enlarge_factor.setter
    def enlarge_factor(self, value: OptionalNumber):
        self._set_attr("enlargeFactor", value)

    # enlarge_strategy property
    @property
    def enlarge_strategy(self) -> Optional[CenterPageEnlargeStrategy]:
        """
        Use enlarge_strategy to determine which method to enlarge the center page.
        """
        return self._get_attr("enlargeStrategy")

    @enlarge_strategy.setter
    def enlarge_strategy(self, value: Optional[CenterPageEnlargeStrategy]):
        self._set_attr("enlargeStrategy", value.value if value else None)

    # page_snapping property
    @property
    def page_snapping(self) -> Optional[bool]:
        """
        Set to false to disable page snapping, useful for custom scroll behavior.
        """
        return self._get_attr("pageSnapping")

    @page_snapping.setter
    def page_snapping(self, value: Optional[bool]):
        self._set_attr("pageSnapping", value)

    # scroll_direction property
    @property
    def scroll_direction(self) -> Optional[ScrollDirection]:
        """
        The axis along which the page view scrolls.
        """
        return self._get_attr("scrollDirection")

    @scroll_direction.setter
    def scroll_direction(self, value: Optional[ScrollDirection]):
        self._set_attr("scrollDirection", value.value if value else None)

    # pause_auto_play_on_touch property
    @property
    def pause_auto_play_on_touch(self) -> Optional[bool]:
        """
        If true, the auto play function will be paused when user is interacting with
        the carousel, and will be resumed when user finish interacting.
        """
        return self._get_attr("pauseAutoPlayOnTouch")

    @pause_auto_play_on_touch.setter
    def pause_auto_play_on_touch(self, value: Optional[bool]):
        self._set_attr("pauseAutoPlayOnTouch", value)

    # pause_auto_play_on_manual_navigate property
    @property
    def pause_auto_play_on_manual_navigate(self) -> Optional[bool]:
        """
        If true, the auto play function will be paused when user is calling
        controller's next_page or previous_page or animate_to_page method.
        """
        return self._get_attr("pauseAutoPlayOnManualNavigate")

    @pause_auto_play_on_manual_navigate.setter
    def pause_auto_play_on_manual_navigate(self, value: Optional[bool]):
        self._set_attr("pauseAutoPlayOnManualNavigate", value)

    # pause_auto_play_in_finite_scroll property
    @property
    def pause_auto_play_in_finite_scroll(self) -> Optional[bool]:
        """
        If enable_infinite_scroll is false, and auto_play is true, this option
        decides if the carousel should go to the first item when it reaches the last item.
        """
        return self._get_attr("pauseAutoPlayInFiniteScroll")

    @pause_auto_play_in_finite_scroll.setter
    def pause_auto_play_in_finite_scroll(self, value: Optional[bool]):
        self._set_attr("pauseAutoPlayInFiniteScroll", value)

    # disable_center property
    @property
    def disable_center(self) -> Optional[bool]:
        """
        Whether or not to disable the Center widget for each slide.
        """
        return self._get_attr("disableCenter")

    @disable_center.setter
    def disable_center(self, value: Optional[bool]):
        self._set_attr("disableCenter", value)

    # pad_ends property
    @property
    def pad_ends(self) -> Optional[bool]:
        """
        Whether to add padding to both ends of the list.
        """
        return self._get_attr("padEnds")

    @pad_ends.setter
    def pad_ends(self, value: Optional[bool]):
        self._set_attr("padEnds", value)

    # enable_scroll_events property
    @property
    def enable_scroll_events(self) -> Optional[bool]:
        """
        Whether to enable scroll events. Disabled by default to avoid event spam.
        When enabled, on_scrolled events will be triggered during scrolling.
        """
        return self._get_attr("enableScrollEvents")

    @enable_scroll_events.setter
    def enable_scroll_events(self, value: Optional[bool]):
        self._set_attr("enableScrollEvents", value)

    # Internal event handlers for JSON decoding
    def _on_page_changed_internal(self, e):
        """Internal handler that decodes JSON and calls user handler."""
        if self.__on_page_changed_handler:
            try:
                # Decode JSON data
                data = json.loads(e.data) if isinstance(e.data, str) else e.data
                # Create a new event object with decoded data
                class EventWithData:
                    def __init__(self, data):
                        self.data = data

                event = EventWithData(data)
                self.__on_page_changed_handler(event)
            except (json.JSONDecodeError, AttributeError):
                # Fallback: pass original event if JSON decode fails
                self.__on_page_changed_handler(e)

    def _on_scrolled_internal(self, e):
        """Internal handler that decodes JSON and calls user handler."""
        if self.__on_scrolled_handler:
            try:
                # Decode JSON data
                data = json.loads(e.data) if isinstance(e.data, str) else e.data
                # Create a new event object with decoded data
                class EventWithData:
                    def __init__(self, data):
                        self.data = data

                event = EventWithData(data)
                self.__on_scrolled_handler(event)
            except (json.JSONDecodeError, AttributeError):
                # Fallback: pass original event if JSON decode fails
                self.__on_scrolled_handler(e)

    # Event handlers
    @property
    def on_page_changed(self) -> OptionalControlEventCallable:
        """
        Called whenever the page in the center of the viewport changes.
        Event data contains: {"index": int, "reason": str}
        """
        return self.__on_page_changed_handler

    @on_page_changed.setter
    def on_page_changed(self, handler: OptionalControlEventCallable):
        self.__on_page_changed_handler = handler

    @property
    def on_scrolled(self) -> OptionalControlEventCallable:
        """
        Called whenever the carousel is scrolled (only if enable_scroll_events=True).
        Event data contains:
        {
            "offset": float,        # Normalized offset (0.0 to item_count)
            "raw_offset": float,    # Raw offset from Flutter
            "current_page": int     # Current page index
        }
        Note: Events are throttled to max 10 per second to avoid spam.
        """
        return self.__on_scrolled_handler

    @on_scrolled.setter
    def on_scrolled(self, handler: OptionalControlEventCallable):
        self.__on_scrolled_handler = handler
        # Auto-enable scroll events if a handler is attached
        if handler is not None and not (self.enable_scroll_events or False):
            self.enable_scroll_events = True
            if self.page:
                self.update()
        # Optionally disable when handler removed (keeping current behavior to avoid flicker)
        # elif handler is None and (self.enable_scroll_events or False):
        #     self.enable_scroll_events = False
        #     if self.page:
        #         self.update()

    # Controller methods
    def next_page(self, duration: Optional[int] = 300, curve: Union[AnimationCurve, str, None] = AnimationCurve.LINEAR):
        """
        Animate to the next page.

        Args:
            duration: Animation duration in milliseconds (default: 300)
            curve: Animation curve (AnimationCurve enum or string, default: AnimationCurve.LINEAR)
        """
        curve_value = curve
        if isinstance(curve, AnimationCurve):
            curve_value = curve.value
        elif curve is None:
            curve_value = AnimationCurve.LINEAR.value

        args = {
            "duration": str(duration or 300),
            "curve": curve_value
        }
        return self.invoke_method("next_page", args, wait_for_result=False)

    def previous_page(self, duration: Optional[int] = 300, curve: Union[AnimationCurve, str, None] = AnimationCurve.LINEAR):
        """
        Animate to the previous page.

        Args:
            duration: Animation duration in milliseconds (default: 300)
            curve: Animation curve (AnimationCurve enum or string, default: AnimationCurve.LINEAR)
        """
        curve_value = curve
        if isinstance(curve, AnimationCurve):
            curve_value = curve.value
        elif curve is None:
            curve_value = AnimationCurve.LINEAR.value

        args = {
            "duration": str(duration or 300),
            "curve": curve_value
        }
        return self.invoke_method("previous_page", args, wait_for_result=False)

    def jump_to_page(self, page: int):
        """
        Jump to the given page without animation.

        Args:
            page: The page index to jump to
        """
        args = {"page": str(page)}
        return self.invoke_method("jump_to_page", args, wait_for_result=False)

    def animate_to_page(self, page: int, duration: Optional[int] = 300, curve: Union[AnimationCurve, str, None] = AnimationCurve.LINEAR):
        """
        Animate to the given page.

        Args:
            page: The page index to animate to
            duration: Animation duration in milliseconds (default: 300)
            curve: Animation curve (AnimationCurve enum or string, default: AnimationCurve.LINEAR)
        """
        curve_value = curve
        if isinstance(curve, AnimationCurve):
            curve_value = curve.value
        elif curve is None:
            curve_value = AnimationCurve.LINEAR.value

        args = {
            "page": str(page),
            "duration": str(duration or 300),
            "curve": curve_value
        }
        return self.invoke_method("animate_to_page", args, wait_for_result=False)

    def get_current_page(self):
        """
        Get the current page index.

        Returns:
            The current page index as an integer
        """
        return self.invoke_method("get_current_page", {}, wait_for_result=True)

    def start_auto_play(self):
        """
        Start auto play if it's currently stopped.
        """
        return self.invoke_method("start_auto_play", {}, wait_for_result=False)

    def stop_auto_play(self):
        """
        Stop auto play if it's currently running.
        """
        return self.invoke_method("stop_auto_play", {}, wait_for_result=False)
