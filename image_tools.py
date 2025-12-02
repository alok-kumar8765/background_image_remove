# Image Tools Package
# Below is a complete Python package module implementing:
# 1. Background removal
# 2. Add background color/template
# 3. Enhance image quality
# 4. Resize and compress image
# 5. Resize by custom height*width
#
# This file can be saved as `image_tools.py` and packaged via setup.py or pyproject.toml
# Required libraries:
# - pillow
# - rembg (for background removal)
# - io, os
# - numpy (optional for quality enhancement)
#
# Installation example:
#   pip install pillow rembg numpy
#
# Usage example:
#   from image_tools import ImageProcessor
#   p = ImageProcessor()
#   p.remove_bg("input.jpg", "out.png")
#
# ---------------------------------------------------------------

import os
from PIL import Image, ImageEnhance
from rembg import remove
import io

class ImageProcessor:
    """
    A utility class providing:
    1. Background removal
    2. Background replacement
    3. Image enhancement
    4. Compression (reduce KB size)
    5. Resize with custom height/width
    """

    def __init__(self):
        pass

    # -----------------------------------------------------------
    # 1. REMOVE BACKGROUND
    # -----------------------------------------------------------
    def remove_bg(self, input_path: str, output_path: str):
        """Remove background using rembg library.
        Handles errors and supports PNG transparent output."""
        try:
            with open(input_path, "rb") as i:
                img_data = i.read()
                result = remove(img_data)

            with open(output_path, "wb") as o:
                o.write(result)

        except Exception as e:
            raise RuntimeError(f"Failed to remove background: {e}")

    # -----------------------------------------------------------
    # 2. ADD BACKGROUND COLOR OR TEMPLATE
    # -----------------------------------------------------------
    def add_background(self, input_path: str, output_path: str, bg_color=(255, 255, 255), template_path: str = None):
        """Add background color or apply a template.
        If template_path is provided, it overlays the template."""
        try:
            img = Image.open(input_path).convert("RGBA")

            if template_path:
                bg = Image.open(template_path).convert("RGBA").resize(img.size)
            else:
                bg = Image.new("RGBA", img.size, bg_color + (255,))

            combined = Image.alpha_composite(bg, img)

            combined.convert("RGB").save(output_path, quality=95)
        except Exception as e:
            raise RuntimeError(f"Failed to apply background: {e}")

    # -----------------------------------------------------------
    # 3. ENHANCE IMAGE QUALITY
    # -----------------------------------------------------------
    def enhance_quality(self, input_path: str, output_path: str, sharpness=1.5, contrast=1.3, brightness=1.1):
        """Enhances image using Pillow built-in enhancement modules."""
        try:
            img = Image.open(input_path).convert("RGB")

            # Sharpness
            img = ImageEnhance.Sharpness(img).enhance(sharpness)
            # Contrast
            img = ImageEnhance.Contrast(img).enhance(contrast)
            # Brightness
            img = ImageEnhance.Brightness(img).enhance(brightness)

            img.save(output_path, quality=95)
        except Exception as e:
            raise RuntimeError(f"Failed to enhance quality: {e}")

    # -----------------------------------------------------------
    # 4. RESIZE & COMPRESS TO KB RANGE
    # -----------------------------------------------------------
    def compress_to_size(self, input_path: str, output_path: str, target_kb: int):
        """Compress an image to a target KB size while preserving quality.
        Uses iterative reduction until size < target_kb."""
        try:
            img = Image.open(input_path)
            quality = 95

            # Save iteratively reducing quality
            while True:
                buffer = io.BytesIO()
                img.save(buffer, format="JPEG", quality=quality)
                size_kb = buffer.tell() / 1024

                if size_kb <= target_kb or quality <= 5:
                    with open(output_path, "wb") as f:
                        f.write(buffer.getvalue())
                    break

                quality -= 5  # reduce quality step-by-step

        except Exception as e:
            raise RuntimeError(f"Failed to compress image: {e}")

    # -----------------------------------------------------------
    # 5. CUSTOM RESIZE (HEIGHT * WIDTH)
    # -----------------------------------------------------------
    def resize_dimensions(self, input_path: str, output_path: str, width: int, height: int):
        """Resize image to custom dimensions with high-quality LANCZOS filter."""
        try:
            img = Image.open(input_path)
            resized = img.resize((width, height), Image.LANCZOS)
            resized.save(output_path, quality=95)
        except Exception as e:
            raise RuntimeError(f"Failed to resize image: {e}")

