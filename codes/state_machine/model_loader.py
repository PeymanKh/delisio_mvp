# Import libraries
import os
import numpy as np
from PIL import Image
import tensorflow as tf


def load_model():
    """
    Loads the pre-trained TensorFlow model for food classification.

    Returns:
        model: Loaded TensorFlow model.
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    model_path = os.path.join(project_root, "models", "fine_tuned_food_classifier.h5")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    model = tf.keras.models.load_model(model_path)
    return model

def preprocess_image(image_path: str) -> np.ndarray:
    """
    Preprocesses an image for the model.

    Args:
        image_path (str): Path to the input image.

    Returns:
        np.ndarray: Preprocessed image ready for model prediction.
    """
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array