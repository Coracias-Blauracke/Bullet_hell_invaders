from game_area.area_object import AreaObject


class Shot(AreaObject):


    def __init__(self, position, movement_speed, radius, angle):
        super().__init__(position)
        self.movement_speed = movement_speed
        self.radius = radius
        self.angle = angle

    def update(self, delta_time):
        raise NotImplementedError