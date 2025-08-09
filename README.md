# 🎠 Flet Carousel Slider

A powerful Flet extension that wraps the Flutter `carousel_slider` package, bringing beautiful and highly customizable carousels to Python applications with Flet.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Flet](https://img.shields.io/badge/Flet-0.28.3+-green.svg)](https://flet.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ Features

### 🎯 **Core Functionality**
- **Auto-play** with customizable intervals and smooth animations
- **Multiple enlarge strategies** (scale, zoom, height) for center page emphasis
- **Infinite scroll** support for seamless navigation
- **Bidirectional scrolling** (horizontal and vertical)
- **Event handling** with page change and scroll callbacks
- **Native Flutter performance** with Python simplicity

### 🎨 **Customization Options**
- **Viewport control** - adjust how many items are visible
- **Animation curves** - choose from 30+ built-in animation types
- **Aspect ratios** - perfect fit for any layout
- **Clip behaviors** - control how content is clipped
- **Pause controls** - pause on touch, manual navigation, etc.
- **Page snapping** - smooth transitions between pages

### 🔧 **Advanced Features**
- **Real-time parameter updates** - change settings dynamically
- **Event data access** - `data.index`, `data.position` attribute-style access
- **Backward compatibility** - supports both new and legacy APIs
- **Null-safe** - robust error handling
- **Performance optimized** - efficient rendering and updates

## 📦 Installation

### Git Dependency

Add to your `pyproject.toml`:

```toml
dependencies = [
  "flet-carousel-slider @ git+https://github.com/skeletorflet/flet-carousel-slider",
  "flet>=0.28.3",
]
```

### PyPI Dependency (when published)

```toml
dependencies = [
  "flet-carousel-slider",
  "flet>=0.28.3",
]
```

### Build Your App

```bash
flet build macos -v
```

## 🚀 Quick Start

### Basic Carousel

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider

def main(page: ft.Page):
    page.title = "My Carousel App"

    # Create carousel items
    items = []
    colors = [ft.Colors.RED, ft.Colors.BLUE, ft.Colors.GREEN, ft.Colors.ORANGE]

    for i, color in enumerate(colors):
        item = ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.STAR, size=50, color=ft.Colors.WHITE),
                ft.Text(f"Page {i+1}", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=color,
            border_radius=15,
            padding=20,
            alignment=ft.alignment.center,
        )
        items.append(item)

    # Create carousel with auto-play
    carousel = FletCarouselSlider(
        items=items,
        height=300,
        auto_play=True,
        auto_play_interval=3000,
        enlarge_center_page=True,
        viewport_fraction=0.8,
    )

    page.add(carousel)

ft.app(main)
```

### Advanced Usage with Events

```python
import flet as ft
from flet_carousel_slider import FletCarouselSlider, CenterPageEnlargeStrategy

def main(page: ft.Page):
    status = ft.Text("Ready")

    def on_page_changed(data):
        # New attribute-style access
        status.value = f"Page: {data.index}, Reason: {data.reason}"
        page.update()

    def on_scrolled(data):
        print(f"Scroll position: {data.position}")

    carousel = FletCarouselSlider(
        items=create_items(),
        height=350,
        auto_play=True,
        auto_play_animation=ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT),
        enlarge_center_page=True,
        enlarge_strategy=CenterPageEnlargeStrategy.SCALE,
        enable_scroll_events=True,
        on_page_changed=on_page_changed,
        on_scrolled=on_scrolled,
    )

    page.add(status, carousel)

ft.app(main)
```

## 📚 Documentation

**[Complete Documentation](https://skeletorflet.github.io/flet-carousel-slider/)**

### 📖 **Key Classes**

| Class | Description |
|-------|-------------|
| `FletCarouselSlider` | Main carousel control with all configuration options |
| `CenterPageEnlargeStrategy` | Enum for center page enlargement strategies |
| `ScrollDirection` | Enum for scroll direction (horizontal/vertical) |
| `EventData` | Event data object with attribute-style access |

## 🎮 Examples

### 📁 **Available Examples**
- **`examples/flet_carousel_slider_example/`** - Interactive demo with real-time controls
- **`examples/complete_demo.py`** - Multiple carousel configurations
- **`examples/advanced_features.py`** - Real-world use cases
- **`examples/attribute_access_demo.py`** - New event API demonstration

### 🎛️ **Interactive Demo**
Run the interactive demo to experiment with all parameters:

```bash
python examples/flet_carousel_slider_example/src/main.py
```

## 🔄 Migration Guide

### From Dict-style to Attribute-style Events

**Old API:**
```python
def on_page_changed(e):
    data = e.data
    index = data['index']
    reason = data['reason']
```

**New API (Recommended):**
```python
def on_page_changed(data):
    index = data.index      # ✨ Attribute access
    reason = data.reason    # ✨ Cleaner syntax
```

## 📄 License

MIT License

## 🙏 Acknowledgments

- Built on [Flutter carousel_slider package](https://pub.dev/packages/carousel_slider)
- Powered by [Flet](https://flet.dev)

---

**Made with ❤️ for the Flet community**
