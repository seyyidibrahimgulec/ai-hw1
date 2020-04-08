from modules.stack import Stack
from modules.point import Point
from modules.img import read_image
from modules.timer import Timer
import time


def astar(start_point=None, end_point=None):
    image = read_image()

    if not start_point:
        start_point = [
            int(n)
            for n in input(
                'Please enter the start point in "x y" format without quotes: '
            ).split()
        ]
    start_point = Point(*start_point, *image.getpixel(tuple(start_point)))
    if not end_point:
        end_point = [
            int(n)
            for n in input(
                'Please enter the end point in "x y" format without quotes: '
            ).split()
        ]
    end_point = Point(*end_point, *image.getpixel(tuple(end_point)))

    timer = Timer()

    stack = Stack()

    stack.push(start_point)

    while stack.length() > 0 and stack.pop() != end_point:
        for point in stack.last_pop.get_neighbours(image):
            stack.push(point)
        stack.red_sort(end_point)

    current_point = stack.last_pop
    while current_point.parent:
        image.putpixel((current_point.x, current_point.y), (0, 255, 0))
        current_point = current_point.parent

    image.show()

    timer.print()
