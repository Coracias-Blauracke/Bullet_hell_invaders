from game_area.point import Point


class PointFactory:

    def create_point(self, x, y):
        return Point(x, y)