"""
Resizes all images in the split dataset folders (train/val/test) to 224x224.

Author: Peyman Khodabandehlouei
"""
# Import libraries
import os
from PIL import Image
from tqdm import tqdm

# Fixed size for model input
TARGET_SIZE = (224, 224)

def resize_images_in_folder(folder_path: str):
    """
    Recursively resizes all images in the given folder to TARGET_SIZE.

    Args:
        folder_path (str): Path to the root folder (train, val, or test)
    """
    image_extensions = ('.jpg', '.jpeg', '.png')

    for root, _, files in os.walk(folder_path):
        for file in tqdm(files, desc=f"Resizing in {os.path.basename(root)}"):
            if file.lower().endswith(image_extensions):
                full_path = os.path.join(root, file)
                try:
                    img = Image.open(full_path)
                    img = img.convert("RGB")
                    img = img.resize(TARGET_SIZE)
                    img.save(full_path)
                except Exception as e:
                    print(f"Error resizing {full_path}: {e}")


def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    split_dir = os.path.join(base_dir, "data", "split")

    for split in ["train", "val", "test"]:
        folder_path = os.path.join(split_dir, split)
        print(f"Processing {folder_path}")
        resize_images_in_folder(folder_path)

    print("All images resized to 224x224.")


if __name__ == "__main__":
    main()
