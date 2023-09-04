from PIL import Image
import requests
from io import BytesIO

def load_image_from_url(url: str) -> Image.Image:
    """
    Load an image from a URL.
    """
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        return image
    except Exception as e:
        print(f"An error occurred while loading image from URL: {e}")
        return None

def load_image_from_file(file_path: str) -> Image.Image:
    """
    Load an image from a file.
    """
    try:
        image = Image.open(file_path)
        return image
    except Exception as e:
        print(f"An error occurred while loading image from file: {e}")
        return None

def validate_image(image: Image.Image) -> bool:
    """
    Validate if the input is a proper image.
    """
    if image:
        return True
    else:
        return False
