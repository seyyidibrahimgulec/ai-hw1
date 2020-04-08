import sys
from PIL import Image


def read_image():
    try:
        return Image.open(input("Please enter an image path: "))
    except IOError:
        sys.exit("Unable to load image.")
