# Introduction

FletCarouselSlider for Flet.

## Examples

```
import flet as ft

from flet_carousel_slider import FletCarouselSlider


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=FletCarouselSlider(
                    tooltip="My new FletCarouselSlider Control tooltip",
                    value = "My new FletCarouselSlider Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[FletCarouselSlider](FletCarouselSlider.md)


