#!/usr/bin/env python3

import flet as ft
from flet_carousel_slider import FletCarouselSlider, ScrollDirection, CenterPageEnlargeStrategy

def main(page: ft.Page):
    page.title = "Flet Carousel Slider Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = "auto"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Create carousel items
    carousel_items = []
    colors = [ft.Colors.RED, ft.Colors.BLUE, ft.Colors.GREEN, ft.Colors.ORANGE, ft.Colors.PURPLE, ft.Colors.YELLOW, ft.Colors.PURPLE, ft.Colors.BLACK]
    
    for i, color in enumerate(colors):
        item = ft.Container(
            content=ft.Column([
                ft.Text(f"Slide {i+1}", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(f"This is slide number {i+1}", size=16, color=ft.Colors.WHITE),
                ft.Icon(ft.Icons.STAR, size=50, color=ft.Colors.WHITE),
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=color,
            border_radius=10,
            padding=20,
            margin=ft.margin.symmetric(horizontal=5),
        )
        carousel_items.append(item)

    # Current page indicator
    current_page_text = ft.Text("Current page: 0", size=16, weight=ft.FontWeight.BOLD)

    def on_page_changed(e):
        data = e.data
        current_page_text.value = f"Current page: {data.get('index', 0)} (Reason: {data.get('reason', 'unknown')})"
        page.update()

    def on_scrolled(e):
        data = e.data
        print(f"Scroll - Page: {data.get('current_page', 0)}, Offset: {data.get('offset', 0):.2f}")

    # Create carousel slider
    carousel = FletCarouselSlider(
        items=carousel_items,
        height=300,
        auto_play=True,
        auto_play_interval=3000,  # 3 seconds
        auto_play_animation_duration=800,
        enlarge_center_page=True,
        enlarge_factor=0.3,
        enlarge_strategy=CenterPageEnlargeStrategy.SCALE,
        viewport_fraction=0.8,
        enable_infinite_scroll=True,
        enable_scroll_events=True,  # Enable scroll events
        on_page_changed=on_page_changed,
        on_scrolled=on_scrolled,
    )

    # Control buttons
    def next_page(e):
        carousel.next_page(duration=500, curve="easeInOut")

    def previous_page(e):
        carousel.previous_page(duration=500, curve="easeInOut")

    def jump_to_first(e):
        carousel.jump_to_page(0)

    def animate_to_last(e):
        carousel.animate_to_page(len(carousel_items) - 1, duration=1000, curve="bounceOut")

    def toggle_auto_play(e):
        if e.control.text == "Stop Auto Play":
            carousel.stop_auto_play()
            e.control.text = "Start Auto Play"
        else:
            carousel.start_auto_play()
            e.control.text = "Stop Auto Play"
        page.update()

    # Button controls
    controls_row = ft.Row([
        ft.ElevatedButton("Previous", on_click=previous_page),
        ft.ElevatedButton("Next", on_click=next_page),
        ft.ElevatedButton("Jump to First", on_click=jump_to_first),
        ft.ElevatedButton("Animate to Last", on_click=animate_to_last),
        ft.ElevatedButton("Stop Auto Play", on_click=toggle_auto_play),
    ], alignment=ft.MainAxisAlignment.CENTER)

    # Create a second carousel with different settings
    simple_items = [
        ft.Container(
            content=ft.Text(f"Item {i}", size=20, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_400,
            border_radius=5,
            padding=20,
            alignment=ft.alignment.center,
        ) for i in range(1, 6)
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
            content=ft.Column([
                ft.Image(
                    src=url,
                    width=350,
                    height=200,
                    fit=ft.ImageFit.COVER,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Text(f"Image {i+1}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            bgcolor=ft.Colors.BLACK54,
            border_radius=10,
            padding=15,
            margin=ft.margin.symmetric(horizontal=5),
        )
        image_items.append(image_item)

    image_carousel = FletCarouselSlider(
        items=image_items,
        height=280,
        auto_play=True,
        auto_play_interval=4000,
        enlarge_center_page=True,
        enlarge_factor=0.2,
        viewport_fraction=0.85,
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
                content=ft.Column([
                    ft.Icon(ft.Icons.SHOPPING_BAG, size=50, color=ft.Colors.WHITE),
                    ft.Text(data["title"], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(data["price"], size=16, color=ft.Colors.WHITE70),
                    ft.ElevatedButton("Buy Now", bgcolor=ft.Colors.WHITE, color=data["color"]),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
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
            content=ft.Row([
                ft.Icon(ft.Icons.STAR, size=30, color=ft.Colors.YELLOW),
                ft.Column([
                    ft.Text(f"Review {i+1}", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("This is an amazing product! Highly recommended.", size=14),
                ], spacing=5, expand=True),
            ], spacing=15),
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

    page.add(
        ft.Column([
            ft.Text("🎠 Flet Carousel Slider Demo", size=28, weight=ft.FontWeight.BOLD),
            ft.Divider(),

            # Main carousel
            ft.Text("🎯 Main Carousel (Auto-play, Enlarge Center)", size=18, weight=ft.FontWeight.W_500),
            carousel,
            current_page_text,
            controls_row,
            ft.Divider(),

            # Image carousel
            ft.Text("🖼️ Image Carousel", size=18, weight=ft.FontWeight.W_500),
            image_carousel,
            ft.Divider(),

            # Card carousel
            ft.Text("🛍️ Product Cards Carousel", size=18, weight=ft.FontWeight.W_500),
            card_carousel,
            ft.Divider(),

            # Vertical carousel
            ft.Text("📝 Vertical Reviews Carousel", size=18, weight=ft.FontWeight.W_500),
            vertical_carousel,
            ft.Divider(),

            # Simple carousel
            ft.Text("🔹 Simple Carousel", size=18, weight=ft.FontWeight.W_500),
            simple_carousel,
        ], spacing=20, scroll=ft.ScrollMode.AUTO, width=500, horizontal_alignment=ft.MainAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)
