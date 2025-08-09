# 🎮 Examples Gallery

This page showcases various use cases and implementations of the Flet Carousel Slider.

## 🚀 Basic Examples

### Simple Carousel

The most basic implementation with minimal configuration:

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider

def main(page: ft.Page):
    page.title = "Simple Carousel"
    
    # Create simple items
    items = [
        ft.Container(
            content=ft.Text(f"Page {i+1}", size=32, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_400,
            border_radius=10,
            padding=30,
            alignment=ft.alignment.center,
        )
        for i in range(5)
    ]
    
    # Basic carousel
    carousel = FletCarouselSlider(
        items=items,
        height=200,
    )
    
    page.add(carousel)

ft.app(main)
```

### Auto-Play Carousel

Carousel with automatic page transitions:

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider

def main(page: ft.Page):
    page.title = "Auto-Play Carousel"
    
    colors = [ft.Colors.RED_400, ft.Colors.GREEN_400, ft.Colors.BLUE_400, ft.Colors.ORANGE_400]
    
    items = [
        ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.STAR, size=50, color=ft.Colors.WHITE),
                ft.Text(f"Auto Page {i+1}", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=colors[i],
            border_radius=15,
            padding=20,
            alignment=ft.alignment.center,
        )
        for i in range(4)
    ]
    
    carousel = FletCarouselSlider(
        items=items,
        height=300,
        auto_play=True,
        auto_play_interval=2000,  # 2 seconds
        auto_play_animation=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
        enlarge_center_page=True,
        viewport_fraction=0.8,
    )
    
    page.add(carousel)

ft.app(main)
```

## 🎨 Advanced Examples

### Image Gallery

A beautiful image gallery with enlarge effects:

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider, CenterPageEnlargeStrategy

def main(page: ft.Page):
    page.title = "Image Gallery"
    
    # Create image items (replace with actual image URLs)
    image_urls = [
        "https://picsum.photos/400/300?random=1",
        "https://picsum.photos/400/300?random=2",
        "https://picsum.photos/400/300?random=3",
        "https://picsum.photos/400/300?random=4",
    ]
    
    items = []
    for i, url in enumerate(image_urls):
        item = ft.Container(
            content=ft.Stack([
                ft.Image(
                    src=url,
                    width=350,
                    height=250,
                    fit=ft.ImageFit.COVER,
                    border_radius=ft.border_radius.all(15),
                ),
                ft.Container(
                    content=ft.Text(f"Photo {i+1}", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.with_opacity(0.7, ft.Colors.BLACK),
                    padding=10,
                    border_radius=ft.border_radius.only(bottom_left=15, bottom_right=15),
                    alignment=ft.alignment.bottom_center,
                ),
            ]),
            border_radius=15,
        )
        items.append(item)
    
    carousel = FletCarouselSlider(
        items=items,
        height=300,
        auto_play=True,
        auto_play_interval=4000,
        enlarge_center_page=True,
        enlarge_strategy=CenterPageEnlargeStrategy.SCALE,
        enlarge_factor=0.3,
        viewport_fraction=0.8,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
    )
    
    page.add(carousel)

ft.app(main)
```

### Product Showcase

A product carousel with interactive elements:

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider, CenterPageEnlargeStrategy

def main(page: ft.Page):
    page.title = "Product Showcase"
    
    products = [
        {"name": "Smartphone Pro", "price": "$999", "color": ft.Colors.BLUE_400},
        {"name": "Laptop Ultra", "price": "$1299", "color": ft.Colors.GREEN_400},
        {"name": "Tablet Max", "price": "$699", "color": ft.Colors.ORANGE_400},
        {"name": "Watch Smart", "price": "$399", "color": ft.Colors.PURPLE_400},
    ]
    
    def create_product_card(product):
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Icon(ft.Icons.DEVICES, size=60, color=ft.Colors.WHITE),
                    bgcolor=product["color"],
                    border_radius=50,
                    width=100,
                    height=100,
                    alignment=ft.alignment.center,
                ),
                ft.Text(product["name"], size=18, weight=ft.FontWeight.BOLD),
                ft.Text("⭐⭐⭐⭐⭐", size=16),
                ft.Text(product["price"], size=20, weight=ft.FontWeight.BOLD, color=product["color"]),
                ft.ElevatedButton("Buy Now", bgcolor=product["color"], color=ft.Colors.WHITE),
            ], 
            alignment=ft.MainAxisAlignment.CENTER, 
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.GREY_100,
            border_radius=20,
            padding=25,
            border=ft.border.all(2, ft.Colors.GREY_300),
        )
    
    items = [create_product_card(product) for product in products]
    
    carousel = FletCarouselSlider(
        items=items,
        height=350,
        auto_play=False,  # Manual navigation for products
        enlarge_center_page=True,
        enlarge_strategy=CenterPageEnlargeStrategy.ZOOM,
        enlarge_factor=0.2,
        viewport_fraction=0.6,
    )
    
    page.add(carousel)

ft.app(main)
```

### Vertical Testimonials

A vertical carousel for testimonials:

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider, ScrollDirection

def main(page: ft.Page):
    page.title = "Customer Testimonials"
    
    testimonials = [
        {"text": "Amazing product! Highly recommended.", "author": "John D."},
        {"text": "Great quality and fast delivery.", "author": "Sarah M."},
        {"text": "Excellent customer service.", "author": "Mike R."},
        {"text": "Best purchase I've made this year!", "author": "Lisa K."},
    ]
    
    items = []
    for testimonial in testimonials:
        item = ft.Container(
            content=ft.Column([
                ft.Text(f'"{testimonial["text"]}"', size=16, italic=True, text_align=ft.TextAlign.CENTER),
                ft.Text("⭐⭐⭐⭐⭐", size=18, text_align=ft.TextAlign.CENTER),
                ft.Text(f"- {testimonial['author']}", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ], spacing=10),
            bgcolor=ft.Colors.BLUE_50,
            border_radius=15,
            padding=20,
            border=ft.border.all(1, ft.Colors.BLUE_200),
        )
        items.append(item)
    
    carousel = FletCarouselSlider(
        items=items,
        height=150,
        scroll_direction=ScrollDirection.VERTICAL,
        auto_play=True,
        auto_play_interval=3000,
        viewport_fraction=0.8,
        enlarge_center_page=False,
    )
    
    page.add(carousel)

ft.app(main)
```

## 🎛️ Interactive Examples

### Event Handling

Carousel with comprehensive event handling:

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider

def main(page: ft.Page):
    page.title = "Event Handling Demo"
    
    status = ft.Text("Ready", size=16, weight=ft.FontWeight.BOLD)
    
    def on_page_changed(data):
        # New attribute-style access
        status.value = f"Page: {data.index}, Reason: {data.reason}"
        page.update()
    
    def on_scrolled(data):
        print(f"Scroll position: {data.position}")
    
    items = [
        ft.Container(
            content=ft.Text(f"Page {i}", size=24, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_400,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center,
        )
        for i in range(5)
    ]
    
    carousel = FletCarouselSlider(
        items=items,
        height=200,
        auto_play=True,
        enable_scroll_events=True,
        on_page_changed=on_page_changed,
        on_scrolled=on_scrolled,
    )
    
    page.add(status, carousel)

ft.app(main)
```

### Manual Controls

Carousel with custom navigation buttons:

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider

def main(page: ft.Page):
    page.title = "Manual Controls"
    
    items = [
        ft.Container(
            content=ft.Text(f"Page {i}", size=24, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.GREEN_400,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center,
        )
        for i in range(6)
    ]
    
    carousel = FletCarouselSlider(
        items=items,
        height=200,
        auto_play=False,
        enlarge_center_page=True,
    )
    
    # Control buttons
    def next_page(e):
        carousel.next_page(ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT))
    
    def previous_page(e):
        carousel.previous_page(ft.Animation(500, ft.AnimationCurve.BOUNCE_OUT))
    
    def jump_to_first(e):
        carousel.jump_to_page(0)
    
    def animate_to_last(e):
        carousel.animate_to_page(len(items)-1, ft.Animation(1000, ft.AnimationCurve.ELASTIC_OUT))
    
    controls = ft.Row([
        ft.ElevatedButton("← Previous", on_click=previous_page),
        ft.ElevatedButton("Next →", on_click=next_page),
        ft.ElevatedButton("First", on_click=jump_to_first),
        ft.ElevatedButton("Last", on_click=animate_to_last),
    ], alignment=ft.MainAxisAlignment.CENTER)
    
    page.add(carousel, controls)

ft.app(main)
```

## 🔧 Configuration Examples

### All Parameters Demo

A comprehensive example showing most configuration options:

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider, CenterPageEnlargeStrategy, ScrollDirection

def main(page: ft.Page):
    page.title = "Full Configuration Demo"
    
    items = [
        ft.Container(
            content=ft.Text(f"Item {i}", size=20, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_400,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center,
        )
        for i in range(8)
    ]
    
    carousel = FletCarouselSlider(
        items=items,
        height=300,
        aspect_ratio=16/9,
        viewport_fraction=0.85,
        initial_page=2,
        enable_infinite_scroll=True,
        animate_to_closest=True,
        reverse=False,
        auto_play=True,
        auto_play_interval=3000,
        auto_play_animation=ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT_CUBIC),
        enlarge_center_page=True,
        enlarge_factor=0.3,
        enlarge_strategy=CenterPageEnlargeStrategy.SCALE,
        page_snapping=True,
        scroll_direction=ScrollDirection.HORIZONTAL,
        pause_auto_play_on_touch=True,
        pause_auto_play_on_manual_navigate=True,
        pause_auto_play_in_finite_scroll=False,
        disable_center=False,
        pad_ends=True,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        enable_scroll_events=True,
        on_page_changed=lambda data: print(f"Page changed: {data.index}"),
        on_scrolled=lambda data: print(f"Scrolled: {data.position}"),
    )
    
    page.add(carousel)

ft.app(main)
```

---

**For more examples, check out the interactive demo:**
```bash
python examples/flet_carousel_slider_example/src/main.py
```
