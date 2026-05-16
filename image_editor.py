from PIL import Image, ImageFilter, ImageEnhance
import os

def edit_image(input_path, output_path, operation):
    """
    Bewerk afbeeldingen met PIL

    Operations:
    - resize: (width, height)
    - blur: intensity (1-10)
    - brighten: intensity (0.5-2.0)
    - contrast: intensity (0.5-2.0)
    - grayscale
    - rotate: degrees
    """

    try:
        # Open afbeelding
        img = Image.open(input_path)

        # Operatie uitvoeren
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
            img = img.convert('L')

        elif operation["type"] == "rotate":
            img = img.rotate(operation["degrees"])

        # Sla op
        img.save(output_path)
        print(f"✅ Afbeelding opgeslagen: {output_path}")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# Voorbeelden
if __name__ == "__main__":
    # Test: maak een voorbeeldafbeelding
    test_img = Image.new('RGB', (200, 200), color='red')
    test_img.save('test_image.jpg')

    print("Test afbeelding aangemaakt!")
    print("\nVoorbeelden:")
    print("1. Verklein:")
    edit_image('test_image.jpg', 'output_small.jpg', {"type": "resize", "width": 100, "height": 100})

    print("\n2. Maak grijsschaal:")
    edit_image('test_image.jpg', 'output_gray.jpg', {"type": "grayscale"})

    print("\n3. Maak helderder:")
    edit_image('test_image.jpg', 'output_bright.jpg', {"type": "brighten", "intensity": 1.5})
