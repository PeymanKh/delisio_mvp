"""
Splits the raw food image dataset into train/val/test subsets.

Each class folder in data/raw/food_dataset/ is split and copied into:
- data/split/train/
- data/split/val/
- data/split/test/

Author: Peyman Khodabandehlouei
"""
# Import libraries
import os
import splitfolders


def main():
    # Define input/output paths
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    input_folder = os.path.join(base_dir, "raw")
    output_folder = os.path.join(base_dir, "split")

    print(f"Splitting dataset from:\n  {input_folder}\ninto:\n  {output_folder}\n")

    # Split using 80% train, 10% val, 10% test
    splitfolders.ratio(
        input_folder,
        output=output_folder,
        seed=42,
        ratio=(.8, .1, .1),
        group_prefix=None,
        move=False
    )

    print("Dataset split completed.")


if __name__ == "__main__":
    main()
