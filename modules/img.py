import sys
from PIL import Image


def read_image(path=None):
    try:
        return Image.open(path if path else input("Please enter an image path: "))
    except IOError:
        sys.exit("Unable to load image.")
