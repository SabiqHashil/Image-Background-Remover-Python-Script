# Image Background Remover & Enhancer

This Python script automates the process of removing backgrounds from images, upscaling them, and enhancing their quality (sharpness, contrast, and color).

## Features

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

1. **Prepare your image**: Place your input image in the project directory. By default, the script looks for `input.jpg`.
2. **Run the script**:
   ```bash
   python background_remover.py
   ```
3. **Check the output**: The processed image will be saved as `output.png` in the same directory.

### Customization

You can modify the `background_remover.py` file to change default settings at the bottom of the script:

```python
if __name__ == "__main__":
    input_image_path = "input.jpg"  # Change input filename
    output_image_path = "output.png" # Change output filename
    
    remove_background_enhance_and_upscale(
        input_image_path, 
        output_image_path, 
        scale=2  # Change upscaling factor (e.g., 4)
    )
```
