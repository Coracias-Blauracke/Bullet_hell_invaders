class GameObject:

    def update(self, delta_time):
        raise NotImplementedError
    
    def draw(self, display):
        raise NotImplementedError