"""
Image scraping script for food classification project.

Uses GoogleImageCrawler to download images for each food class
and saves them into the correct project directory structure.

Author: Peyman Khodabandehlouei
"""
# Import libraries
import os
import time
import logging
from icrawler.builtin import BingImageCrawler

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

FOOD_CLASSES = [
    "fried chicken", "kebab", "paella", "pasta", "burger",
    "pizza", "ramen", "steak", "sushi", "tacos", "unknown"
]

def get_dataset_base_dir() -> str:
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    dataset_path = os.path.join(project_root, "data", "raw")
    os.makedirs(dataset_path, exist_ok=True)
    return dataset_path


def download_images(query: str, save_dir: str, max_num: int = 1000):
    os.makedirs(save_dir, exist_ok=True)

    crawler = BingImageCrawler(storage={'root_dir': save_dir})

    try:
        crawler.crawl(keyword=query, max_num=max_num, file_idx_offset='auto')
    except Exception as e:
        logging.error(f"Error scraping '{query}': {e}")


def scrape_all_classes(max_num: int = 1000):
    start_time = time.time()
    base_dir = get_dataset_base_dir()
    logging.info(f"Saving all images to: {base_dir}")

    for food_class in FOOD_CLASSES:
        query = f"{food_class} food" if food_class != "unknown" else "random food, object, background"
        class_folder = food_class.replace(" ", "_").lower()
        save_path = os.path.join(base_dir, class_folder)

        logging.info(f"Crawling: '{query}' | Saving to: {save_path}")
        download_images(query, save_path, max_num=max_num)

        count = len(os.listdir(save_path))
        logging.info(f"Downloaded {count} images for '{food_class}'\n")

    duration = time.time() - start_time
    logging.info(f"Finished scraping in {duration:.2f} seconds.")


if __name__ == "__main__":
    scrape_all_classes()
