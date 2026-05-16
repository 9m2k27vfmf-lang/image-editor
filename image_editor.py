from PIL import Image, ImageFilter, ImageEnhance


def edit_image(input_path: str, output_path: str, operation: dict) -> bool:
    """
    Apply an image operation using PIL and save the result.

    Operations:
    - resize: requires 'width' (int) and 'height' (int)
    - blur: requires 'intensity' (1-10)
    - brighten: requires 'intensity' (0.5-2.0)
    - contrast: requires 'intensity' (0.5-2.0)
    - grayscale: no extra fields needed
    - rotate: requires 'degrees' (int)

    Returns True on success, False on failure.
    """
    try:
        img = Image.open(input_path)

        if operation["type"] == "resize":
            img = img.resize((operation["width"], operation["height"]))

        elif operation["type"] == "blur":
            img = img.filter(ImageFilter.GaussianBlur(radius=operation["intensity"]))

        elif operation["type"] == "brighten":
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(operation["intensity"])

        elif operation["type"] == "contrast":
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(operation["intensity"])

        elif operation["type"] == "grayscale":
            img = img.convert("L")

        elif operation["type"] == "rotate":
            img = img.rotate(operation["degrees"])

        img.save(output_path)
        print(f"Saved: {output_path}")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    test_img = Image.new("RGB", (200, 200), color="red")
    test_img.save("test_image.jpg")
    print("Test image created.")

    print("\nExamples:")
    print("1. Resize:")
    edit_image("test_image.jpg", "output_small.jpg", {"type": "resize", "width": 100, "height": 100})

    print("\n2. Grayscale:")
    edit_image("test_image.jpg", "output_gray.jpg", {"type": "grayscale"})

    print("\n3. Brighten:")
    edit_image("test_image.jpg", "output_bright.jpg", {"type": "brighten", "intensity": 1.5})

