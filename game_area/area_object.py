from game_control.game_object import GameObject


class AreaObject(GameObject):
    
    def __init__(self, position):
        self.position = position

    def update(self):
        raise NotImplementedError
    
    def draw(self):
        raise NotImplementedError