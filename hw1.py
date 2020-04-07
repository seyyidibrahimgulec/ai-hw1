import sys

from PIL import Image


directory = input("Please enter the image path :")

try:
    im = Image.open(directory)

except IOError:
    print("Unable to load image")
    sys.exit(1)

mat = im.load()
width, height = im.size


# for x in range(width):
#     for y in range(height):
#         r, g, b = mat[x, y]
#         print(r)
class Homework:
    

def best_first_search(start, end):
    start_x, start_y = start
    end_x, end_y = end
    



def find_max_red(point):
    x, y = point
    max = 0
    next_point = 0, 0

    # Northwest
    if x - 1 > 0 and y - 1 > 0:
        r, g, b = mat[x - 1, y - 1]
        print("Point coordinates: {}, {} -- R value: {}".format(x - 1, y - 1, r))
        if max < r:
            max = r
            next_point = x - 1, y - 1
    # North
    if y - 1 > 0:
        r, g, b = mat[x, y - 1]
        print("Point coordinates: {}, {} -- R value: {}".format(x, y - 1, r))
        if max < r:
            max = r
            next_point = x, y - 1
    # Northeast
    if x + 1 < width and y - 1 > 0:
        r, g, b = mat[x + 1, y - 1]
        print("Point coordinates: {}, {} -- R value: {}".format(x + 1, y - 1, r))
        if max < r:
            max = r
            next_point = x + 1, y - 1
    # East
    if x + 1 < width:
        r, g, b = mat[x + 1, y]
        print("Point coordinates: {}, {} -- R value: {}".format(x + 1, y, r))
        if max < r:
            max = r
            next_point = x + 1, y
    # Southeast
    if x + 1 < width and y + 1 < height:
        r, g, b = mat[x + 1, y + 1]
        print("Point coordinates: {}, {} -- R value: {}".format(x + 1, y + 1, r))
        if max < r:
            max = r
            next_point = x + 1, y + 1
    # South
    if y + 1 < height:
        r, g, b = mat[x, y + 1]
        print("Point coordinates: {}, {} -- R value: {}".format(x, y + 1, r))
        if max < r:
            max = r
            next_point = x, y + 1
    # Southwest
    if x - 1 > 0 and y + 1 < height:
        r, g, b = mat[x - 1, y + 1]
        print("Point coordinates: {}, {} -- R value: {}".format(x - 1, y + 1, r))
        if max < r:
            max = r
            next_point = x - 1, y + 1
    # West
    if x - 1 > 0:
        r, g, b = mat[x - 1, y]
        print("Point coordinates: {}, {} -- R value: {}".format(x - 1, y, r))
        if max < r:
            max = r
            next_point = x - 1, y

    return next_point

def distance(start, end):
    start_x, start_y = start
    end_x, end_y = end
    return ((start_x - end_x) * (start_x - end_x)) +\
        (((start_y - end_y) * (start_y - end_y)))


point = 0, 10
print(find_max_red(point))


# def main():
#     pass


# if __name__ == '__main__':
#     main()
