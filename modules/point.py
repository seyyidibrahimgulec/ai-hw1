class Point:
    """
    x,y ve renk var, uzaklık hesaplayabilir, etrafındaki noktaları hesaplayabilir.
    """

    def __init__(self, x, y, r, g, b, parent=None):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.total_red = (parent.total_red if parent else 0) + (255 -self.r)
        self.parent = parent

    def distance(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y)

    def __str__(self):
        return f"{self.x, self.y, self.r, self.g, self.b}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_neighbours(self, image):
        neighbours = []
        # Northwest
        if self.x - 1 > 0 and self.y - 1 > 0:
            neighbour_coordinate = self.x - 1, self.y - 1
            neighbours.append(
                Point(*neighbour_coordinate, *image.getpixel((neighbour_coordinate)), parent=self)
            )
        # North
        if self.y - 1 > 0:
            neighbour_coordinate = self.x, self.y - 1
            neighbours.append(
                Point(*neighbour_coordinate, *image.getpixel((neighbour_coordinate)), parent=self)
            )
        # Northeast
        if self.x + 1 < image.width and self.y - 1 > 0:
            neighbour_coordinate = self.x + 1, self.y - 1
            neighbours.append(
                Point(*neighbour_coordinate, *image.getpixel((neighbour_coordinate)), parent=self)
            )
        # East
        if self.x + 1 < image.width:
            neighbour_coordinate = self.x + 1, self.y
            neighbours.append(
                Point(*neighbour_coordinate, *image.getpixel((neighbour_coordinate)), parent=self)
            )
        # Southeast
        if self.x + 1 < image.width and self.y + 1 < image.height:
            neighbour_coordinate = self.x + 1, self.y + 1
            neighbours.append(
                Point(*neighbour_coordinate, *image.getpixel((neighbour_coordinate)), parent=self)
            )
        # South
        if self.y + 1 < image.height:
            neighbour_coordinate = self.x, self.y + 1
            neighbours.append(
                Point(*neighbour_coordinate, *image.getpixel((neighbour_coordinate)), parent=self)
            )
        # Southwest
        if self.x - 1 > 0 and self.y + 1 < image.height:
            neighbour_coordinate = self.x - 1, self.y + 1
            neighbours.append(
                Point(*neighbour_coordinate, *image.getpixel((neighbour_coordinate)), parent=self)
            )
        # West
        if self.x - 1 > 0:
            neighbour_coordinate = self.x - 1, self.y
            neighbours.append(
                Point(*neighbour_coordinate, *image.getpixel((neighbour_coordinate)), parent=self)
            )

        return neighbours
