class Point:
    """
    x,y ve renk var, uzaklık hesaplayabilir, etrafındaki noktaları hesaplayabilir.
    """
    def __init__(self, x, y, r, g, b):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b

    def distance(self, point):
        return ((self.x - point.x) * (self.x - point.x)) + (
            ((self.y - point.y) * (self.y - point.y))
        )


# Examples
p1 = Point(20, 16, 0, 0, 0)
p2 = Point(17, 20, 0, 0, 0)
print(p1.distance(p2))
