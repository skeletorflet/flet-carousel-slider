---
type: "manual"
---

#
---
applyTo: '**'
---

#
---
applyTo: '**'
---

# Flet Extension Development Custom Instructions

## Project Overview & Structure

This repository enables the creation of Flet extensions by wrapping Flutter packages for use in Python apps. It provides guides, templates, and working examples for both visual (`ConstrainedControl`) and non-visual (`Control`) controls, including event handling and advanced communication patterns between Python and Dart.

**Key folders:**
- `/package-guide/src/flet_package_guide/`: Python control logic for Flet extensions.
- `/package-guide/src/flutter/flet_package_guide/`: Dart/Flutter code for control implementations.
- `/package-guide/examples/`: Sample Flet apps demonstrating extension usage.
- `/package-guide/docs/`: API and usage documentation.

**Frameworks:** Python >=3.9, Flet >=0.28.3, Dart/Flutter.

## Coding Standards & Extension Patterns

- Map Python control classes to the corresponding Flutter package classes and their properties/events.
- For visual packages, create a Python class inheriting from `ConstrainedControl` and a Dart widget wrapping the package's widget.
- For non-visual packages, create a Python class inheriting from `Control` and a Dart logic class wrapping the package's logic.
- Use property decorators in Python and parse with `attrString`, `attrBool`, `attrDouble`, etc. in Dart.
- For lists or complex objects, use JSON serialization between Python and Dart.
- Define event callback properties in Python (e.g., `on_something`) and trigger events from Dart using backend calls (`backend.trigger("event_name", data)`).
- Always keep property/event names in sync between Python and Dart.
- Document new controls and events in the repo docs.

## User Package Instruction

Whenever the user provides a random package from pub.dev (visual or non-visual), you must implement the extension fully for Flet usage. This includes:
- Mapping Python control classes to the corresponding Flutter package classes and their properties/events.
- For visual packages, create a Python class inheriting from `ConstrainedControl` and a Dart widget wrapping the package's widget.
- For non-visual packages, create a Python class inheriting from `Control` and a Dart logic class wrapping the package's logic.
- Expose all relevant properties, methods, and events in both Python and Dart, following the patterns in this guide.
- Ensure the extension is ready for use in a Flet app, with all handlers and communication working as described.

## Example: Visual Control

**Python:**
```python
class MyControl(ConstrainedControl):
    def __init__(self, value: str = "", on_change=None):
        super().__init__()
        self.value = value
        self.on_change = on_change

    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, v):
        self._set_attr("value", v)

    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler):
        self._set_event_handler("change", handler)
```

**Dart:**
```dart
class MyControlWidget extends StatefulWidget {
  final Control control;
  final FletControlBackend backend;

  @override
  Widget build(BuildContext context) {
    String value = control.attrString("value", "");
    return TextField(
      controller: TextEditingController(text: value),
      onChanged: (newValue) {
        backend.trigger("change", {"value": newValue});
      },
    );
  }
}
```

## Example: Non-Visual Control

**Python:**
```python
class MyLogicControl(Control):
    def __init__(self, on_tick=None):
        super().__init__()
        self.on_tick = on_tick

    @property
    def on_tick(self):
        return self._get_event_handler("tick")

    @on_tick.setter
    def on_tick(self, handler):
        self._set_event_handler("tick", handler)
```

**Dart:**
```dart
class MyLogicControl {
  final Control control;
  final FletControlBackend backend;

  void startPeriodic() {
    Timer.periodic(Duration(seconds: 1), (timer) {
      backend.trigger("tick", {"counter": timer.tick});
    });
  }
}
```

## Advanced Patterns

- For async callbacks, periodic events, progress updates, and timeout handling, use Dart's async features and communicate with Python using backend triggers and JSON data.
- Always keep property/event names in sync between Python and Dart.
- Document new controls and events in the repo docs.

## Trust These Instructions

- Only search the codebase if information is missing or errors occur.
- Focus on coding the extension and Python-Dart relationship, not build or environment setup.
# Copilot Instructions for flet-package-guide

## High-Level Overview

- **Purpose:** This repository enables the creation of Flet extensions by wrapping Flutter packages for use in Python apps via Flet. It provides a guide, templates, and working examples for both visual (`ConstrainedControl`) and non-visual (`Control`) controls, including event handling and advanced communication patterns.
- **Tech Stack:**  
  - **Python** (>=3.9) for Flet control logic  
  - **Dart/Flutter** for UI and control implementation  
  - **Flet** (>=0.28.3) as the Python-UI bridge  
  - **MkDocs** for documentation  
  - **Poetry/uv** for dependency management  
- **Repo Size:** Medium, with clear separation between Python, Dart, and documentation assets.

## Project Layout

- **Root Files:**  
  - `README.md` (extension development guide)  
  - `package-guide/` (main package)  
    - `src/flet_package_guide/` (Python control logic)  
    - `src/flutter/flet_package_guide/` (Dart/Flutter code)  
    - `docs/` (API and usage docs)  
    - `examples/` (sample Flet apps)  
    - `pyproject.toml`, `mkdocs.yml` (config)  
- **Key Source Files:**  
  - `src/flet_package_guide/flet_package_guide.py` (Python control implementation)  
  - `src/flutter/flet_package_guide/lib/src/flet_package_guide.dart` (Dart control implementation)  
  - `examples/flet_package_guide_example/src/main.py` (Python app example)  
- **Configuration:**  
  - Python: `pyproject.toml`  
  - Dart/Flutter: `pubspec.yaml`  
  - Docs: `mkdocs.yml`  
- **Testing:**  
  - Example app in `examples/`  
  - No explicit CI/CD, but always validate changes by running the example app.



# Copilot Instructions for Flet Extension Coding

## Purpose

This repository is for creating Flet extensions by wrapping Flutter packages for use in Python apps. The main goal is to connect Python (Flet) controls to Dart (Flutter) widgets, supporting both visual (`ConstrainedControl`) and non-visual (`Control`) types, with event handling and advanced communication.

## User Package Instruction

Whenever the user provides a random package from pub.dev (visual or non-visual), you must implement the extension fully for Flet usage. This includes:
- Mapping Python control classes to the corresponding Flutter package classes and their properties/events.
- For visual packages, create a Python class inheriting from `ConstrainedControl` and a Dart widget wrapping the package's widget.
- For non-visual packages, create a Python class inheriting from `Control` and a Dart logic class wrapping the package's logic.
- Expose all relevant properties, methods, and events in both Python and Dart, following the patterns in this guide.
- Ensure the extension is ready for use in a Flet app, with all handlers and communication working as described.

## How Python and Dart Relate

- **Visual Controls:**
  - Inherit from `ConstrainedControl` in Python.
  - Implement a corresponding Dart widget class.
  - Pass properties and children from Python to Dart using JSON serialization.

- **Non-Visual Controls:**
  - Inherit from `Control` in Python.
  - Implement a logic-only Dart class (no UI).

- **Property Mapping:**
  - In Python, use property decorators for each attribute.
  - In Dart, parse properties using methods like `attrString`, `attrBool`, `attrDouble`, etc.
  - For lists or complex objects, use JSON and parse in Dart with `json.decode`.

- **Event Handlers:**
  - In Python, define event callback properties (e.g., `on_something`).
  - In Dart, trigger events using backend calls (`backend.trigger("event_name", data)`), which invoke the Python handler.
  - For periodic or async events, use Dart timers or async methods and send updates to Python.

## Coding a New Extension (pub.dev package)

1. **Add the Dart package to `pubspec.yaml` and run `flutter pub get`.**
2. **Create a Dart widget/class in `lib/src/` that wraps the package's functionality.**
3. **Expose properties and events in Dart using the Flet control API.**
4. **Create a Python control class in `src/flet_package_guide/` inheriting from `ConstrainedControl` or `Control`.**
5. **Map Python properties to Dart attributes using property decorators and `_set_attr`/`_set_attr_json`.**
6. **For events, define Python handler properties and trigger them from Dart using backend calls.**
7. **For complex data, use JSON for serialization between Python and Dart.**
8. **Test the extension in a sample Flet app (see `examples/`).**

## Example: Visual Control

**Python:**
```python
class MyControl(ConstrainedControl):
    def __init__(self, value: str = "", on_change=None):
        super().__init__()
        self.value = value
        self.on_change = on_change

    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, v):
        self._set_attr("value", v)

    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler):
        self._set_event_handler("change", handler)
```

**Dart:**
```dart
class MyControlWidget extends StatefulWidget {
  final Control control;
  final FletControlBackend backend;

  @override
  Widget build(BuildContext context) {
    String value = control.attrString("value", "");
    return TextField(
      controller: TextEditingController(text: value),
      onChanged: (newValue) {
        backend.trigger("change", {"value": newValue});
      },
    );
  }
}
```

## Example: Non-Visual Control

**Python:**
```python
class MyLogicControl(Control):
    def __init__(self, on_tick=None):
        super().__init__()
        self.on_tick = on_tick

    @property
    def on_tick(self):
        return self._get_event_handler("tick")

    @on_tick.setter
    def on_tick(self, handler):
        self._set_event_handler("tick", handler)
```

**Dart:**
```dart
class MyLogicControl {
  final Control control;
  final FletControlBackend backend;

  void startPeriodic() {
    Timer.periodic(Duration(seconds: 1), (timer) {
      backend.trigger("tick", {"counter": timer.tick});
    });
  }
}
```

## Advanced Patterns

- For async callbacks, periodic events, progress updates, and timeout handling, use Dart's async features and communicate with Python using backend triggers and JSON data.
- Always keep property/event names in sync between Python and Dart.
- Document new controls and events in the repo docs.

## Trust These Instructions

- Only search the codebase if information is missing or errors occur.
- Focus on coding the extension and Python-Dart relationship, not build or environment setup.