# 🎠 Flet Carousel Slider Documentation

Welcome to the complete documentation for **Flet Carousel Slider** - a powerful extension that brings beautiful, customizable carousels to your Flet applications.

## 🚀 Quick Start

### Installation

```bash
pip install flet-carousel-slider
```

### Basic Usage

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider

def main(page: ft.Page):
    # Create carousel items
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

    # Create carousel
    carousel = FletCarouselSlider(
        items=items,
        height=300,
        auto_play=True,
        enlarge_center_page=True,
    )

    page.add(carousel)

ft.app(main)
```

## 📚 API Reference

### Main Classes

- **[FletCarouselSlider](FletCarouselSlider.md)** - The main carousel control
- **[CenterPageEnlargeStrategy](FletCarouselSlider.md)** - Enlarge strategies enum
- **[ScrollDirection](FletCarouselSlider.md)** - Scroll direction enum
- **[EventData](FletCarouselSlider.md)** - Event data object

## 🎯 Key Features

### ✨ **Auto-Play**
- Customizable intervals (1-8 seconds)
- Smooth animation transitions
- Pause on touch/manual navigation
- Multiple animation curves

### 🎨 **Visual Customization**
- **Enlarge center page** with scale, zoom, or height strategies
- **Viewport fraction** control (0.3-1.0)
- **Aspect ratio** adjustment
- **Clip behaviors** (none, hard edge, anti-alias)

### 🔄 **Navigation**
- **Infinite scroll** support
- **Bidirectional** (horizontal/vertical)
- **Page snapping** for smooth transitions
- **Manual controls** with custom animations

### 📡 **Events**
- **Page change events** with reason tracking
- **Scroll position events** for advanced interactions
- **Attribute-style access** (`data.index`, `data.position`)
- **Backward compatibility** with dict-style access

## 🎮 Interactive Examples

### Real-Time Parameter Control

The package includes an interactive demo that lets you experiment with all parameters in real-time:

```bash
python examples/flet_carousel_slider_example/src/main.py
```

**Features:**
- 🎛️ **Sliders** for height, aspect ratio, viewport fraction
- ☑️ **Checkboxes** for boolean options (auto-play, infinite scroll, etc.)
- 📋 **Dropdowns** for enums (animation curves, enlarge strategies)
- 🔄 **Live updates** - see changes instantly

### Advanced Use Cases

```python
# Image Gallery Carousel
image_carousel = FletCarouselSlider(
    items=image_items,
    height=400,
    auto_play=True,
    auto_play_interval=5000,
    enlarge_center_page=True,
    enlarge_strategy=CenterPageEnlargeStrategy.SCALE,
    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
)

# Vertical Testimonials
testimonial_carousel = FletCarouselSlider(
    items=testimonial_items,
    height=200,
    scroll_direction=ScrollDirection.VERTICAL,
    auto_play=True,
    viewport_fraction=0.8,
)

# Product Showcase
product_carousel = FletCarouselSlider(
    items=product_items,
    height=350,
    auto_play=False,
    enlarge_center_page=True,
    enlarge_strategy=CenterPageEnlargeStrategy.ZOOM,
    on_page_changed=lambda data: print(f"Viewing product {data.index}"),
)
```

## 🔧 Advanced Configuration

### Animation System

Use Flet's powerful animation system:

```python
carousel = FletCarouselSlider(
    items=items,
    auto_play_animation=ft.Animation(
        duration=1200,
        curve=ft.AnimationCurve.EASE_IN_OUT_CUBIC
    ),
)

# Manual navigation with custom animations
carousel.next_page(ft.Animation(800, ft.AnimationCurve.BOUNCE_OUT))
carousel.previous_page(ft.Animation(600, ft.AnimationCurve.ELASTIC_OUT))
carousel.animate_to_page(2, ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT_BACK))
```

### Event Handling

```python
def on_page_changed(data):
    # New attribute-style access (recommended)
    print(f"Page: {data.index}, Reason: {data.reason}")

    # Legacy dict-style access (still supported)
    print(f"Page: {data['index']}, Reason: {data['reason']}")

def on_scrolled(data):
    # Raw position from Flutter carousel_slider
    position = data.position
    print(f"Scroll position: {position}")

carousel = FletCarouselSlider(
    items=items,
    enable_scroll_events=True,
    on_page_changed=on_page_changed,
    on_scrolled=on_scrolled,
)
```

## 🎨 Styling Examples

### Modern Card Layout

```python
def create_card(title, subtitle, color):
    return ft.Container(
        content=ft.Column([
            ft.Icon(ft.Icons.STAR, size=50, color=ft.Colors.WHITE),
            ft.Text(title, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text(subtitle, size=14, color=ft.Colors.WHITE70),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
        bgcolor=color,
        border_radius=20,
        padding=30,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
        ),
    )

cards = [
    create_card("Feature 1", "Description", ft.Colors.BLUE_400),
    create_card("Feature 2", "Description", ft.Colors.GREEN_400),
    create_card("Feature 3", "Description", ft.Colors.ORANGE_400),
]

carousel = FletCarouselSlider(
    items=cards,
    height=300,
    enlarge_center_page=True,
    enlarge_factor=0.3,
    viewport_fraction=0.8,
)
```

## 🔄 Migration Guide

### Upgrading from Dict-style Events

**Before:**
```python
def on_page_changed(e):
    data = e.data
    index = data['index']
    reason = data['reason']
```

**After:**
```python
def on_page_changed(data):
    index = data.index      # ✨ Direct attribute access
    reason = data.reason    # ✨ Cleaner, more Pythonic
```

Both styles are supported for backward compatibility.

## 🤝 Contributing

We welcome contributions! Check out our [GitHub repository](https://github.com/skeletorflet/flet-carousel-slider) for:

- 🐛 **Bug reports**
- 💡 **Feature requests**
- 🔧 **Pull requests**
- 📖 **Documentation improvements**

## 📄 License

This project is licensed under the MIT License.

---

**Ready to create amazing carousels? Check out the [complete API reference](FletCarouselSlider.md)!**


