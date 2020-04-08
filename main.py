from classes.img import read_image
from classes.timer import Timer

import time


if __name__ == "__main__":
    timer = Timer()
    image = read_image()
    image.show()
    timer.print()
    time.sleep(2)
    timer.print()
    time.sleep(2)
    timer.print()
