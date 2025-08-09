#!/usr/bin/env python3

import flet as ft
from flet_carousel_slider import (
    FletCarouselSlider,
    ScrollDirection,
    CenterPageEnlargeStrategy,
)


def main(page: ft.Page):
    page.title = "Flet Carousel Slider Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Create carousel items
    carousel_items = []
    colors = [
        ft.Colors.RED,
        ft.Colors.BLUE,
        ft.Colors.GREEN,
        ft.Colors.ORANGE,
        ft.Colors.PURPLE,
        ft.Colors.YELLOW,
        ft.Colors.PURPLE,
        ft.Colors.BLACK,
    ]

    for i, color in enumerate(colors):
        item = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        f"Slide {i + 1}",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        f"This is slide number {i + 1}", size=16, color=ft.Colors.WHITE
                    ),
                    ft.Icon(ft.Icons.STAR, size=50, color=ft.Colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=color,
            border_radius=10,
            padding=20,
            margin=ft.margin.symmetric(horizontal=5),
        )
        carousel_items.append(item)

    # Current page indicator
    current_page_text = ft.Text("Current page: 0", size=16, weight=ft.FontWeight.BOLD)

    # Carousel reference (will be set later)
    carousel = None

    def on_page_changed(data):
        """Event handler receives data using new attribute access"""
        current_page_text.value = f"Current page: {data.index} (Reason: {data.reason})"
        page.update()

    def on_scrolled(data):
        """Event handler receives data using new attribute access"""
        print(f"Scroll position: {data.position:.2f}")

    # Interactive Controls for Carousel Parameters
    def update_carousel():
        """Recreate carousel with new parameters"""
        nonlocal carousel

        # Get current values from controls
        new_carousel = FletCarouselSlider(
            items=carousel_items,
            height=height_slider.value,
            aspect_ratio=aspect_ratio_slider.value,
            viewport_fraction=viewport_slider.value,
            initial_page=int(initial_page_slider.value),
            enable_infinite_scroll=infinite_scroll_checkbox.value,
            animate_to_closest=animate_closest_checkbox.value,
            reverse=reverse_checkbox.value,
            auto_play=auto_play_checkbox.value,
            auto_play_interval=int(auto_play_interval_slider.value),
            auto_play_animation=ft.Animation(
                int(auto_play_duration_slider.value),
                getattr(ft.AnimationCurve, auto_play_curve_dropdown.value),
            ),
            enlarge_center_page=enlarge_center_checkbox.value,
            enlarge_factor=enlarge_factor_slider.value,
            enlarge_strategy=getattr(
                CenterPageEnlargeStrategy, enlarge_strategy_dropdown.value
            ),
            page_snapping=page_snapping_checkbox.value,
            scroll_direction=getattr(ScrollDirection, scroll_direction_dropdown.value),
            pause_auto_play_on_touch=pause_on_touch_checkbox.value,
            pause_auto_play_on_manual_navigate=pause_on_manual_checkbox.value,
            pause_auto_play_in_finite_scroll=pause_in_finite_checkbox.value,
            disable_center=disable_center_checkbox.value,
            pad_ends=pad_ends_checkbox.value,
            clip_behavior=getattr(ft.ClipBehavior, clip_behavior_dropdown.value),
            enable_scroll_events=scroll_events_checkbox.value,
            on_page_changed=on_page_changed,
            on_scrolled=on_scrolled if scroll_events_checkbox.value else None,
        )

        # Replace carousel in the layout
        carousel_container.content = new_carousel
        carousel = new_carousel
        page.update()

    # Sliders
    height_slider = ft.Slider(
        min=200,
        max=500,
        value=320,
        divisions=30,
        label="Height: {value}",
        on_change=lambda e: update_carousel(),
    )

    aspect_ratio_slider = ft.Slider(
        min=1.0,
        max=3.0,
        value=16 / 9,
        divisions=20,
        label="Aspect: {value:.2f}",
        on_change=lambda e: update_carousel(),
    )

    viewport_slider = ft.Slider(
        min=0.3,
        max=1.0,
        value=0.85,
        divisions=14,
        label="Viewport: {value:.2f}",
        on_change=lambda e: update_carousel(),
    )

    initial_page_slider = ft.Slider(
        min=0,
        max=len(carousel_items) - 1,
        value=1,
        divisions=len(carousel_items) - 1,
        label="Initial Page: {value}",
        on_change=lambda e: update_carousel(),
    )

    auto_play_interval_slider = ft.Slider(
        min=1000,
        max=8000,
        value=3500,
        divisions=14,
        label="Auto Interval: {value}ms",
        on_change=lambda e: update_carousel(),
    )

    auto_play_duration_slider = ft.Slider(
        min=300,
        max=2000,
        value=1000,
        divisions=17,
        label="Auto Duration: {value}ms",
        on_change=lambda e: update_carousel(),
    )

    enlarge_factor_slider = ft.Slider(
        min=0.0,
        max=0.8,
        value=0.35,
        divisions=16,
        label="Enlarge Factor: {value:.2f}",
        on_change=lambda e: update_carousel(),
    )

    # Checkboxes
    infinite_scroll_checkbox = ft.Checkbox(
        label="Enable Infinite Scroll",
        value=True,
        on_change=lambda e: update_carousel(),
    )
    animate_closest_checkbox = ft.Checkbox(
        label="Animate to Closest", value=True, on_change=lambda e: update_carousel()
    )
    reverse_checkbox = ft.Checkbox(
        label="Reverse Direction", value=False, on_change=lambda e: update_carousel()
    )
    auto_play_checkbox = ft.Checkbox(
        label="Auto Play", value=True, on_change=lambda e: update_carousel()
    )
    enlarge_center_checkbox = ft.Checkbox(
        label="Enlarge Center Page", value=True, on_change=lambda e: update_carousel()
    )
    page_snapping_checkbox = ft.Checkbox(
        label="Page Snapping", value=True, on_change=lambda e: update_carousel()
    )
    pause_on_touch_checkbox = ft.Checkbox(
        label="Pause on Touch", value=True, on_change=lambda e: update_carousel()
    )
    pause_on_manual_checkbox = ft.Checkbox(
        label="Pause on Manual Navigate",
        value=True,
        on_change=lambda e: update_carousel(),
    )
    pause_in_finite_checkbox = ft.Checkbox(
        label="Pause in Finite Scroll",
        value=False,
        on_change=lambda e: update_carousel(),
    )
    disable_center_checkbox = ft.Checkbox(
        label="Disable Center", value=False, on_change=lambda e: update_carousel()
    )
    pad_ends_checkbox = ft.Checkbox(
        label="Pad Ends", value=True, on_change=lambda e: update_carousel()
    )
    scroll_events_checkbox = ft.Checkbox(
        label="Enable Scroll Events", value=False, on_change=lambda e: update_carousel()
    )

    # Dropdowns
    auto_play_curve_dropdown = ft.Dropdown(
        label="Auto Play Curve",
        value="EASE_IN_OUT_CUBIC",
        options=[
            ft.dropdown.Option("LINEAR"),
            ft.dropdown.Option("EASE_IN_OUT"),
            ft.dropdown.Option("EASE_IN_OUT_CUBIC"),
            ft.dropdown.Option("BOUNCE_OUT"),
            ft.dropdown.Option("ELASTIC_OUT"),
            ft.dropdown.Option("FAST_OUT_SLOWIN"),
        ],
        on_change=lambda e: update_carousel(),
    )

    enlarge_strategy_dropdown = ft.Dropdown(
        label="Enlarge Strategy",
        value="SCALE",
        options=[
            ft.dropdown.Option("SCALE"),
            ft.dropdown.Option("ZOOM"),
            ft.dropdown.Option("HEIGHT"),
        ],
        on_change=lambda e: update_carousel(),
    )

    scroll_direction_dropdown = ft.Dropdown(
        label="Scroll Direction",
        value="HORIZONTAL",
        options=[
            ft.dropdown.Option("HORIZONTAL"),
            ft.dropdown.Option("VERTICAL"),
        ],
        on_change=lambda e: update_carousel(),
    )

    clip_behavior_dropdown = ft.Dropdown(
        label="Clip Behavior",
        value="ANTI_ALIAS",
        options=[
            ft.dropdown.Option("NONE"),
            ft.dropdown.Option("HARD_EDGE"),
            ft.dropdown.Option("ANTI_ALIAS"),
            ft.dropdown.Option("ANTI_ALIAS_WITH_SAVE_LAYER"),
        ],
        on_change=lambda e: update_carousel(),
    )

    # Create initial carousel
    carousel = FletCarouselSlider(
        items=carousel_items,
        height=height_slider.value,
        aspect_ratio=aspect_ratio_slider.value,
        viewport_fraction=viewport_slider.value,
        initial_page=int(initial_page_slider.value),
        enable_infinite_scroll=infinite_scroll_checkbox.value,
        animate_to_closest=animate_closest_checkbox.value,
        reverse=reverse_checkbox.value,
        auto_play=auto_play_checkbox.value,
        auto_play_interval=int(auto_play_interval_slider.value),
        auto_play_animation=ft.Animation(
            int(auto_play_duration_slider.value),
            getattr(ft.AnimationCurve, auto_play_curve_dropdown.value),
        ),
        enlarge_center_page=enlarge_center_checkbox.value,
        enlarge_factor=enlarge_factor_slider.value,
        enlarge_strategy=getattr(
            CenterPageEnlargeStrategy, enlarge_strategy_dropdown.value
        ),
        page_snapping=page_snapping_checkbox.value,
        scroll_direction=getattr(ScrollDirection, scroll_direction_dropdown.value),
        pause_auto_play_on_touch=pause_on_touch_checkbox.value,
        pause_auto_play_on_manual_navigate=pause_on_manual_checkbox.value,
        pause_auto_play_in_finite_scroll=pause_in_finite_checkbox.value,
        disable_center=disable_center_checkbox.value,
        pad_ends=pad_ends_checkbox.value,
        clip_behavior=getattr(ft.ClipBehavior, clip_behavior_dropdown.value),
        enable_scroll_events=scroll_events_checkbox.value,
        on_page_changed=on_page_changed,
        on_scrolled=on_scrolled if scroll_events_checkbox.value else None,
    )

    # Container for carousel (for easy replacement)
    carousel_container = ft.Container(content=carousel)

    # Control buttons with various animation types
    def next_page_smooth(e):
        carousel.next_page(ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT))

    def previous_page_bounce(e):
        carousel.previous_page(ft.Animation(800, ft.AnimationCurve.BOUNCE_OUT))

    def next_page_elastic(e):
        carousel.next_page(ft.Animation(1200, ft.AnimationCurve.ELASTIC_OUT))

    def previous_page_fast(e):
        carousel.previous_page(ft.Animation(300, ft.AnimationCurve.FAST_OUT_SLOWIN))

    def jump_to_first(e):
        carousel.jump_to_page(0)

    def animate_to_middle(e):
        middle_page = len(carousel_items) // 2
        carousel.animate_to_page(
            middle_page, ft.Animation(1500, ft.AnimationCurve.EASE_IN_OUT_BACK)
        )

    def animate_to_last(e):
        carousel.animate_to_page(
            len(carousel_items) - 1, ft.Animation(1000, ft.AnimationCurve.BOUNCE_OUT)
        )

    def no_animation_next(e):
        carousel.next_page(False)  # No animation

    def toggle_auto_play(e):
        if e.control.text == "Stop Auto Play":
            carousel.stop_auto_play()
            e.control.text = "Start Auto Play"
            e.control.bgcolor = ft.Colors.GREEN_600
        else:
            carousel.start_auto_play()
            e.control.text = "Stop Auto Play"
            e.control.bgcolor = ft.Colors.RED_600
        page.update()

    # Button controls with different animation styles
    controls_row1 = ft.Row(
        [
            ft.ElevatedButton(
                "← Smooth", on_click=next_page_smooth, bgcolor=ft.Colors.BLUE_600
            ),
            ft.ElevatedButton(
                "Bounce →", on_click=previous_page_bounce, bgcolor=ft.Colors.ORANGE_600
            ),
            ft.ElevatedButton(
                "← Elastic", on_click=next_page_elastic, bgcolor=ft.Colors.PURPLE_600
            ),
            ft.ElevatedButton(
                "Fast →", on_click=previous_page_fast, bgcolor=ft.Colors.GREEN_600
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        wrap=True,
    )

    controls_row2 = ft.Row(
        [
            ft.ElevatedButton(
                "Jump to First", on_click=jump_to_first, bgcolor=ft.Colors.GREY_600
            ),
            ft.ElevatedButton(
                "Go to Middle", on_click=animate_to_middle, bgcolor=ft.Colors.TEAL_600
            ),
            ft.ElevatedButton(
                "Animate to Last",
                on_click=animate_to_last,
                bgcolor=ft.Colors.INDIGO_600,
            ),
            ft.ElevatedButton(
                "No Animation →",
                on_click=no_animation_next,
                bgcolor=ft.Colors.BROWN_600,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        wrap=True,
    )

    controls_row3 = ft.Row(
        [
            ft.ElevatedButton(
                "Stop Auto Play", on_click=toggle_auto_play, bgcolor=ft.Colors.RED_600
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Create a second carousel with different settings
    simple_items = [
        ft.Container(
            content=ft.Text(f"Item {i}", size=20, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_400,
            border_radius=5,
            padding=20,
            alignment=ft.alignment.center,
        )
        for i in range(1, 6)
    ]

    simple_carousel = FletCarouselSlider(
        items=simple_items,
        height=150,
        viewport_fraction=0.6,
        enlarge_center_page=False,
        auto_play=False,
        scroll_direction=ScrollDirection.HORIZONTAL,
    )

    # Layout
    # Image Carousel Example
    image_items = []
    image_urls = [
        "https://picsum.photos/400/300?random=1",
        "https://picsum.photos/400/300?random=2",
        "https://picsum.photos/400/300?random=3",
        "https://picsum.photos/400/300?random=4",
        "https://picsum.photos/400/300?random=5",
    ]

    for i, url in enumerate(image_urls):
        image_item = ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src=url,
                        width=350,
                        height=200,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(10),
                    ),
                    ft.Text(
                        f"Image {i + 1}",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor=ft.Colors.BLACK54,
            border_radius=10,
            padding=15,
            margin=ft.margin.symmetric(horizontal=5),
            expand=True,
        )
        image_items.append(image_item)

    image_carousel = FletCarouselSlider(
        items=image_items,
        height=280,
        auto_play=True,
        auto_play_interval=4000,
        enlarge_center_page=True,
        enlarge_factor=0.5,
        viewport_fraction=0.45,
    )

    # Card Carousel Example
    card_items = []
    card_data = [
        {"title": "Product 1", "price": "$29.99", "color": ft.Colors.BLUE_400},
        {"title": "Product 2", "price": "$39.99", "color": ft.Colors.GREEN_400},
        {"title": "Product 3", "price": "$19.99", "color": ft.Colors.ORANGE_400},
        {"title": "Product 4", "price": "$49.99", "color": ft.Colors.PURPLE_400},
        {"title": "Product 5", "price": "$24.99", "color": ft.Colors.RED_400},
    ]

    for data in card_data:
        card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.SHOPPING_BAG, size=50, color=ft.Colors.WHITE),
                        ft.Text(
                            data["title"],
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        ),
                        ft.Text(data["price"], size=16, color=ft.Colors.WHITE70),
                        ft.ElevatedButton(
                            "Buy Now", bgcolor=ft.Colors.WHITE, color=data["color"]
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                bgcolor=data["color"],
                padding=20,
                border_radius=10,
                width=200,
                height=180,
            ),
            elevation=5,
        )
        card_items.append(card)

    card_carousel = FletCarouselSlider(
        items=card_items,
        height=220,
        viewport_fraction=0.6,
        enlarge_center_page=False,
        auto_play=False,
    )

    # Vertical Carousel Example
    vertical_items = []
    for i in range(4):
        item = ft.Container(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.STAR, size=30, color=ft.Colors.YELLOW),
                    ft.Column(
                        [
                            ft.Text(
                                f"Review {i + 1}", size=18, weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "This is an amazing product! Highly recommended.",
                                size=14,
                            ),
                        ],
                        spacing=5,
                        expand=True,
                    ),
                ],
                spacing=15,
            ),
            bgcolor=ft.Colors.GREY_100,
            border_radius=8,
            padding=15,
            margin=ft.margin.symmetric(vertical=5),
        )
        vertical_items.append(item)

    vertical_carousel = FletCarouselSlider(
        items=vertical_items,
        height=200,
        scroll_direction=ScrollDirection.VERTICAL,
        auto_play=True,
        auto_play_interval=3000,
        viewport_fraction=0.7,
    )

    # Layout with interactive controls
    page.add(
        ft.Row([
            # Left side - Controls
            ft.Container(
                content=ft.Column([
                    ft.Text("�️ Interactive Controls", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text("Adjust parameters to see real-time changes", size=14, color=ft.Colors.GREY_600),

                    ft.Divider(),

                    # Sliders Section
                    ft.Text("📏 Size & Layout", size=16, weight=ft.FontWeight.BOLD),
                    ft.Text("Height", size=12, weight=ft.FontWeight.BOLD),
                    height_slider,
                    ft.Text("Aspect Ratio", size=12, weight=ft.FontWeight.BOLD),
                    aspect_ratio_slider,
                    ft.Text("Viewport Fraction", size=12, weight=ft.FontWeight.BOLD),
                    viewport_slider,
                    ft.Text("Initial Page", size=12, weight=ft.FontWeight.BOLD),
                    initial_page_slider,
                    ft.Text("Enlarge Factor", size=12, weight=ft.FontWeight.BOLD),
                    enlarge_factor_slider,

                    ft.Divider(),

                    # Auto Play Section
                    ft.Text("⏱️ Auto Play", size=16, weight=ft.FontWeight.BOLD),
                    auto_play_checkbox,
                    ft.Text("Auto Play Interval", size=12, weight=ft.FontWeight.BOLD),
                    auto_play_interval_slider,
                    ft.Text("Auto Play Duration", size=12, weight=ft.FontWeight.BOLD),
                    auto_play_duration_slider,
                    auto_play_curve_dropdown,

                    ft.Divider(),

                    # Behavior Section
                    ft.Text("⚙️ Behavior", size=16, weight=ft.FontWeight.BOLD),
                    infinite_scroll_checkbox,
                    animate_closest_checkbox,
                    reverse_checkbox,
                    enlarge_center_checkbox,
                    page_snapping_checkbox,

                    ft.Divider(),

                    # Advanced Section
                    ft.Text("� Advanced", size=16, weight=ft.FontWeight.BOLD),
                    pause_on_touch_checkbox,
                    pause_on_manual_checkbox,
                    pause_in_finite_checkbox,
                    disable_center_checkbox,
                    pad_ends_checkbox,
                    scroll_events_checkbox,

                    ft.Divider(),

                    # Dropdowns Section
                    ft.Text("🎨 Style & Direction", size=16, weight=ft.FontWeight.BOLD),
                    enlarge_strategy_dropdown,
                    scroll_direction_dropdown,
                    clip_behavior_dropdown,

                ], spacing=8, scroll=ft.ScrollMode.AUTO, expand=True),
                width=350,
                padding=20,
                bgcolor=ft.Colors.GREY_50,
                border_radius=10,
            ),

            # Right side - Carousel and Animation Controls
            ft.Container(
                content=ft.Column([
                    ft.Text("🎠 Interactive Carousel Demo", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Use the controls on the left to modify the carousel in real-time!",
                           size=16, color=ft.Colors.GREY_600),

                    ft.Divider(),

                    current_page_text,
                    carousel_container,

                    ft.Divider(),

                    ft.Text("🎮 Animation Controls", size=16, weight=ft.FontWeight.BOLD),
                    controls_row1,
                    controls_row2,
                    controls_row3,

                    ft.Divider(),

                    ft.Container(
                        content=ft.Column([
                            ft.Text("� Tips", size=16, weight=ft.FontWeight.BOLD),
                            ft.Text("• Try different enlarge strategies with enlarge_center_page enabled"),
                            ft.Text("• Adjust viewport_fraction to see more/fewer items"),
                            ft.Text("• Enable scroll_events to see position data in console"),
                            ft.Text("• Change scroll_direction to vertical for different layouts"),
                            ft.Text("• Experiment with different animation curves for auto-play"),
                        ], spacing=5),
                        bgcolor=ft.Colors.BLUE_50,
                        padding=15,
                        border_radius=8,
                        border=ft.border.all(1, ft.Colors.BLUE_200),
                    ),

                ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll="auto"),
                expand=True,
                padding=20,
            ),

        ], expand=True, spacing=0)
    )


if __name__ == "__main__":
    ft.app(target=main)
