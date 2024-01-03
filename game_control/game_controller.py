from game_control.game_object import GameObject


class GameController(GameObject):

    def __init__(self):
        self.objects = []

    def update(self, delta_time):
        for object in self.objects:
            object.update(delta_time)
    
    def draw(self, display):
        for object in self.objects:
            object.draw(display)

    def add_object(self, object):
        self.objects.append(object)