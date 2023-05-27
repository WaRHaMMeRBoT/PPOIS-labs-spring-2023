
class Coord2d:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def __add__(self, other):
        return Coord2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord2d(self.x - other.x, self.y - other.y)

    def __cmp__(self, other):
        return (self.x == other.x) and (self.y == other.y)


def get_coord_radius(coord1, coord2):
    diff = coord1 - coord2
    x, y = abs(diff.x, diff.y)
    return min(x, y)
