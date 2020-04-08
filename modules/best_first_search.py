from modules.stack import Stack
from modules.point import Point
from modules.img import read_image
from modules.timer import Timer


def bfs(start_point=None, end_point=None):
    image = read_image("test.jpg")

    if not start_point:
        start_point = [
            int(n)
            for n in input(
                'Please enter the start point in "x y" format without quotes: '
            ).split()
        ]
    if not end_point:
        end_point = [
            int(n)
            for n in input(
                'Please enter the end point in "x y" format without quotes: '
            ).split()
        ]

    # ...
