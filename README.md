# Image Background Remover & Enhancer

This Python script automates the process of removing backgrounds from images, upscaling them, and enhancing their quality (sharpness, contrast, and color).

## Features

- **Dual Processing Modes**:
  - **Remove Background & Upscale**: Standard full processing.
  - **Upscale Only**: Enhanced image upscaling without removing the background.
- **Background Removal**: Utilizes the `rembg` library for accurate background removal.
- **Image Upscaling**: Increases image resolution (default 2x) using high-quality Lanczos resampling.
- **Image Enhancement**:
  - Increases Sharpness (1.6x)
  - Boosts Contrast (1.2x)
  - Enriches Color (1.1x)

## Prerequisites

- Python 3.8+ installed on your system.

## Setup & Installation

It is best practice to run this project in a virtual environment to manage dependencies.

### 1. Create and Activate Virtual Environment

**Windows (PowerShell/Command Prompt):**
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

### 2. Install Dependencies

Once the virtual environment is active, install the required packages:

```bash
pip install rembg pillow
```

## Usage

1. **Prepare your image**: Place your input image in the project directory.
2. **Run the script**:
   
   **Interactive Mode:**
   Simply run the script and follow the prompts:
   ```bash
   python image_processor.py
   ```
   You will be asked to:
   1. **Select Mode**:
      - `1`: **Remove Background & Upscale** (Standard behavior)
      - `2`: **Upscale Only** (Keeps background, only enhances quality)
   2. **Input image path**: The path to your image file.
   3. **Output image path**: Where to save the result.
   4. **Upscaling factor**: Choose `2`, `4`, or `8`.

   **Command Line Interface (CLI):**
   You can pass arguments directly, including the new mode flag:
   ```bash
   python image_processor.py -m 2 -i input.jpg -o output.png -s 4
   ```

   **Arguments:**
   - `-m`, `--mode`: Processing mode (`1` = Remove BG + Upscale, `2` = Upscale Only).
   - `-i`, `--input`: Path to input image.
   - `-o`, `--output`: Path to save output image.
   - `-s`, `--scale`: Upscaling factor (`2`, `4`, `8`).

3. **Check the output**: The processed image will be saved to your specified output path.

### Notes

- **First Run**: The first time you run `rembg` (Mode 1), it will download the U2NET model (approx. 170MB). Upscale Only mode does not require this.
- **File Size**: The output is saved as an optimized PNG. No file size limit is currently enforced.
