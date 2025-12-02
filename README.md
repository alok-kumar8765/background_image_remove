# Background Image Removal

**This is complete Python package module implementing: 1 - Background removal, 2 - Add background color/template. 3 -  Enhance image quality, 4 - Resize and compress image, 5 - Resize by custom height*width**

---

# 📦 **Image Magic Suite – The Ultimate Python Image Processing Toolkit**

### ⭐ Background Removal • Smart Background Add • AI-Ready Enhancement • Compression • Resize • Quality Boost

*(SEO-optimized description with tags included)*

---

## 🧩 **What is Image Magic Suite?**

**Image Magic Suite** is a powerful, production-ready Python package designed for modern image processing needs.
It provides all essential features in a single, lightweight module:

### ✅ Background Removal (powered by `rembg`)

### ✅ Add Background Colors or Templates

### ✅ Image Quality Enhancement (sharpness, contrast, brightness)

### ✅ Compress Large Images (1 MB → 20–90 KB) Without Visible Quality Loss

### ✅ Custom Resize (Height × Width) With High-Quality LANCZOS Filter

This package is ideal for:

* E-commerce product photo optimization
* ID photo editing
* Social media content apps
* SaaS products
* Bulk image processing pipelines
* Automation workflows
* AI datasets preprocessing

---

## 🚀 **Features Included**

### 🔹 **1. Background Removal**

Uses the popular `rembg` AI engine to remove backgrounds cleanly and produce transparent PNG output.

### 🔹 **2. Add Background Color or Templates**

Apply plain colors or a custom background template (overlay).

### 🔹 **3. Enhance Image Quality**

Improve sharpness, brightness & contrast using Pillow’s enhancement tools.

### 🔹 **4. Compress Images to Target File Size**

Automatically reduce file size (KB range) while trying to preserve visual quality.

### 🔹 **5. Custom Resize (Height × Width)**

Resize with **LANCZOS** (best image quality for downscaling).

---

## 🔧 **Installation**

```bash
pip install pillow rembg numpy
```

---

## 🧪 **Example Usage**

```python
from image_tools import ImageProcessor

processor = ImageProcessor()

processor.remove_bg("input.jpg", "output.png")
processor.add_background("input.png", "bg_added.jpg", bg_color=(255,255,255))
processor.enhance_quality("input.jpg", "enhanced.jpg")
processor.compress_to_size("input.jpg", "compressed.jpg", target_kb=80)
processor.resize_dimensions("input.jpg", "resized.jpg", width=800, height=600)
```

---

## 🗂 **Included Module Description (`image_tools.py`)**

This module contains complete implementations for:

### ✔ Background Removal

Reads image → passes to rembg → writes transparent PNG.

### ✔ Apply Background

Add solid color or template overlay (RGBA alpha composite).

### ✔ Enhancement

Boosts sharpness, brightness, contrast with Pillow.

### ✔ Compression

Iteratively reduces quality until reaching target size in KB.

### ✔ Resize

Uses high-quality LANCZOS filter to preserve clarity.

All functions have **error handling**, **clean code**, **PEP8 compliant**, and **clear docstrings**.

---

