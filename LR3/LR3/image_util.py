from pathlib import Path
from os import path


def get_image(file_name):
    root = Path(path.dirname(__file__)) / "img" / file_name
    if root.exists():
        return str(root)
    else:
        return "No image"
