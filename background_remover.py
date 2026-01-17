from rembg import remove
from PIL import Image, ImageEnhance
import sys
import time
import os
import argparse

# Define all the steps in order
STEPS = [
    "Opening image",
    "Removing background",
    "Upscaling image",
    "Enhancing sharpness",
    "Enhancing contrast",
    "Enhancing color",
    "Saving final image"
]

def print_progress(step_index, total_steps):
    """Print a progress bar and steps status in the console"""
    percent = int((step_index / total_steps) * 100)
    bar = "#" * (percent // 2) + "-" * (50 - percent // 2)

    # Build steps status
    status_lines = ""
    for i, step in enumerate(STEPS):
        if i < step_index:
            status_lines += f"✔ {step}\n"
        elif i == step_index:
            status_lines += f"➤ {step}\n"
        else:
            status_lines += f"  {step}\n"

    # Print the progress bar and steps
    sys.stdout.write("\033c")  # Clear console
    sys.stdout.write(f"[{bar}] {percent}%\n")
    sys.stdout.write(status_lines)
    sys.stdout.flush()


def remove_background_enhance_and_upscale(input_path, output_path, scale=2):
    """
    Remove background, upscale image, and enhance quality using PIL only.
    """
    total_steps = len(STEPS)

    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"❌ Error: Input file '{input_path}' not found.")
        return

    try:
        # Step 1: Open image
        print_progress(0, total_steps)
        input_image = Image.open(input_path).convert("RGBA")
        time.sleep(0.5)

        # Step 2: Remove background
        print_progress(1, total_steps)
        bg_removed = remove(input_image)
        time.sleep(0.5)

        # Step 3: Upscale image
        print_progress(2, total_steps)
        width, height = bg_removed.size
        new_size = (width * scale, height * scale)
        upscaled_image = bg_removed.resize(new_size, resample=Image.LANCZOS)
        time.sleep(0.5)

        # Step 4: Enhance sharpness
        print_progress(3, total_steps)
        sharpness = ImageEnhance.Sharpness(upscaled_image)
        upscaled_image = sharpness.enhance(1.6)
        time.sleep(0.3)

        # Step 5: Enhance contrast
        print_progress(4, total_steps)
        contrast = ImageEnhance.Contrast(upscaled_image)
        upscaled_image = contrast.enhance(1.2)
        time.sleep(0.3)

        # Step 6: Enhance color
        print_progress(5, total_steps)
        color = ImageEnhance.Color(upscaled_image)
        upscaled_image = color.enhance(1.1)
        time.sleep(0.3)

        # Step 7: Save final image
        print_progress(6, total_steps)
        upscaled_image.save(output_path, format="PNG", optimize=True)
        time.sleep(0.3)

        # Complete
        print_progress(total_steps, total_steps)
        print(f"\n✅ Background removed, image upscaled, and enhanced successfully!\nSaved to: {output_path}")

    except Exception as e:
        print(f"❌ Error during processing: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove background and upscale images with enhancements.")
    parser.add_argument("-i", "--input", help="Path to input image")
    parser.add_argument("-o", "--output", help="Path to save output image")
    parser.add_argument("-s", "--scale", type=int, choices=[2, 4, 8], help="Upscaling factor (2, 4, 8)")

    args = parser.parse_args()

    # Interactive fallback if arguments are missing
    input_path = args.input
    if not input_path:
        input_path = input("Enter input image path: ").strip().strip('"').strip("'")

    output_path = args.output
    if not output_path:
        output_path = input("Enter output image path (default: upscaled.png): ").strip().strip('"').strip("'")
        if not output_path:
            output_path = "upscaled.png"

    scale = args.scale
    if scale is None:
        scale_input = input("Enter upscaling factor (2, 4, 8) [default: 2]: ").strip()
        if scale_input in ["2", "4", "8"]:
            scale = int(scale_input)
        else:
            scale = 2

    print("\nStarting background removal and upscaling...")
    remove_background_enhance_and_upscale(input_path, output_path, scale)
