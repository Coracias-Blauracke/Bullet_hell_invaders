from game_area.shots.simple_shot import SimpleShot


class ShotFactory:

    def __init__(self, point_factory):
        self.point_factory = point_factory

    def create_simple_shot(self, position, movement_speed = 100, radius = 5, angle = 0, color='red'):
        return SimpleShot(
            self.point_factory.create_point(position.x, position.y),
            movement_speed,
            radius,
            angle,
            color)