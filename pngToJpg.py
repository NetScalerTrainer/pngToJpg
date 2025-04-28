from PIL import Image
import os
import glob

# Find all files matching "cd_*.png" in the current directory
png_files = glob.glob('cd_*.png')

# Output directory (optional)
output_dir = 'converted_jpgs'
os.makedirs(output_dir, exist_ok=True)

for png_file in png_files:
    try:
        # Open the PNG image
        with Image.open(png_file) as img:
            # Convert to RGB mode (to handle transparency)
            rgb_img = img.convert('RGB')
            # Create the new filename
            base_name = os.path.splitext(os.path.basename(png_file))[0]
            jpg_filename = os.path.join(output_dir, base_name + '.jpg')
            # Save as JPEG
            rgb_img.save(jpg_filename, 'JPEG')
            print(f"Converted {png_file} -> {jpg_filename}")
    except Exception as e:
        print(f"Failed to convert {png_file}: {e}")

if not png_files:
    print("No files matching 'cd_*.png' found.")
