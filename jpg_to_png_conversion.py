import os
from PIL import Image

# Ensure given directory for the jpg images is correct.
while True:
    jpg_folder = input("Please provide the file path for the jpg images: ")

    if not os.path.exists(jpg_folder):
        print("This file path does not exist.")
        continue

    break


png_folder = input("Please provide a file path for"
                   "the png images to be saved to: ")

# Create the file path for png images if given path does not exist.
if not os.path.exists(png_folder):
    os.makedirs(png_folder)


IMAGE_CONVERSION_COUNT = 1

# Iterate through jpg files and convert to png.
for filename in os.listdir(jpg_folder):
    if filename.endswith(".jpg"):
        # obtain file name without extension.
        clean_name = os.path.splitext(filename)[0]
        img = Image.open(f'{jpg_folder}/{filename}')
        img.save(f'{png_folder}/{clean_name}.png', 'png')
        print(f"Image {IMAGE_CONVERSION_COUNT} conversion completed.")
        IMAGE_CONVERSION_COUNT += 1

print("Image conversion complete.")
