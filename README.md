# Image Editor

A lightweight Python image editor built with [Pillow](https://pillow.readthedocs.io/).

## Features

| Operation | Description |
|-----------|-------------|
| `resize` | Scale image to a given width × height |
| `blur` | Apply Gaussian blur |
| `brighten` | Increase or decrease brightness |
| `contrast` | Increase or decrease contrast |
| `grayscale` | Convert to grayscale |
| `rotate` | Rotate by degrees |

## Requirements

```bash
pip3 install pillow
```

## Usage

```python
from image_editor import edit_image

# Resize
edit_image("input.jpg", "output.jpg", {"type": "resize", "width": 800, "height": 600})

# Blur
edit_image("input.jpg", "output.jpg", {"type": "blur", "intensity": 3})

# Brighten
edit_image("input.jpg", "output.jpg", {"type": "brighten", "intensity": 1.5})

# Grayscale
edit_image("input.jpg", "output.jpg", {"type": "grayscale"})

# Rotate
edit_image("input.jpg", "output.jpg", {"type": "rotate", "degrees": 90})
```

## Run demo

```bash
python3 image_editor.py
```

This creates a red test image and applies resize, grayscale, and brighten operations.
