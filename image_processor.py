from rembg import remove
from PIL import Image, ImageEnhance
import sys
import time
import os
import argparse

# Define all the steps in order
# Define all the steps for each mode
STEPS_FULL = [
    "Opening image",
    "Removing background",
    "Upscaling image",
    "Enhancing sharpness",
    "Enhancing contrast",
    "Enhancing color",
    "Saving final image"
]

STEPS_UPSCALE = [
    "Opening image",
    "Upscaling image",
    "Enhancing sharpness",
    "Enhancing contrast",
    "Enhancing color",
    "Saving final image"
]

def print_progress(step_index, total_steps, current_steps):
    """Print a progress bar and steps status in the console"""
    percent = int((step_index / total_steps) * 100)
    bar = "#" * (percent // 2) + "-" * (50 - percent // 2)

    # Build steps status
    status_lines = ""
    for i, step in enumerate(current_steps):
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


def process_image(input_path, output_path, scale=2, remove_bg=True):
    """
    Process image: optional background removal, upscaling, and enhancement.
    """
    current_steps = STEPS_FULL if remove_bg else STEPS_UPSCALE
    total_steps = len(current_steps)

    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"❌ Error: Input file '{input_path}' not found.")
        return

    try:
        step_counter = 0

        # Step: Open image
        print_progress(step_counter, total_steps, current_steps)
        input_image = Image.open(input_path).convert("RGBA")
        step_counter += 1
        time.sleep(0.5)

        # Step: Remove background (Optional)
        processed_image = input_image
        if remove_bg:
            print_progress(step_counter, total_steps, current_steps)
            processed_image = remove(input_image)
            step_counter += 1
            time.sleep(0.5)

        # Step: Upscale image
        print_progress(step_counter, total_steps, current_steps)
        width, height = processed_image.size
        new_size = (width * scale, height * scale)
        upscaled_image = processed_image.resize(new_size, resample=Image.LANCZOS)
        step_counter += 1
        time.sleep(0.5)

        # Step: Enhance sharpness
        print_progress(step_counter, total_steps, current_steps)
        sharpness = ImageEnhance.Sharpness(upscaled_image)
        upscaled_image = sharpness.enhance(1.6)
        step_counter += 1
        time.sleep(0.3)

        # Step: Enhance contrast
        print_progress(step_counter, total_steps, current_steps)
        contrast = ImageEnhance.Contrast(upscaled_image)
        upscaled_image = contrast.enhance(1.2)
        step_counter += 1
        time.sleep(0.3)

        # Step: Enhance color
        print_progress(step_counter, total_steps, current_steps)
        color = ImageEnhance.Color(upscaled_image)
        upscaled_image = color.enhance(1.1)
        step_counter += 1
        time.sleep(0.3)

        # Step: Save final image
        print_progress(step_counter, total_steps, current_steps)
        upscaled_image.save(output_path, format="PNG", optimize=True)
        step_counter += 1
        time.sleep(0.3)

        # Complete
        print_progress(total_steps, total_steps, current_steps)
        print(f"\n✅ Processing complete!\nSaved to: {output_path}")

    except Exception as e:
        print(f"❌ Error during processing: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove background and/or upscale images with enhancements.")
    parser.add_argument("-m", "--mode", type=int, choices=[1, 2], help="Mode: 1 (Remove BG + Upscale), 2 (Upscale Only)")
    parser.add_argument("-i", "--input", help="Path to input image")
    parser.add_argument("-o", "--output", help="Path to save output image")
    parser.add_argument("-s", "--scale", type=int, choices=[2, 4, 8], help="Upscaling factor (2, 4, 8)")

    args = parser.parse_args()

    # Interactive prompt for Mode
    mode = args.mode
    if mode is None:
        print("\nSelect Mode:")
        print("1 - Remove Background & Upscale")
        print("2 - Upscale Only")
        while True:
            mode_input = input("Enter selection (1 or 2): ").strip()
            if mode_input in ["1", "2"]:
                mode = int(mode_input)
                break
            print("Invalid selection. Please enter 1 or 2.")
    
    remove_bg = (mode == 1)

    # Interactive prompt for Input
    input_path = args.input
    if not input_path:
        input_path = input("Enter input image path: ").strip().strip('"').strip("'")

    # Interactive prompt for Output
    output_path = args.output
    if not output_path:
        default_out = "output.png"
        output_path = input(f"Enter output image path (default: {default_out}): ").strip().strip('"').strip("'")
        if not output_path:
            output_path = default_out

    # Interactive prompt for Scale
    scale = args.scale
    if scale is None:
        scale_input = input("Enter upscaling factor (2, 4, 8) [default: 2]: ").strip()
        if scale_input in ["2", "4", "8"]:
            scale = int(scale_input)
        else:
            scale = 2

    print(f"\nStarting processing (Mode: {'Remove BG + Upscale' if remove_bg else 'Upscale Only'})...")
    process_image(input_path, output_path, scale, remove_bg)
