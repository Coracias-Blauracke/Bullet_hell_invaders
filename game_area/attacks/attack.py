from game_control.game_object import GameObject


class Attack(GameObject):

    def __init__(
            self,
            attack_speed,
            number_of_attacks,
            shot_movement_speed,
            spawn_position,
            shot_factory):
        
        self.attack_speed = attack_speed
        self.current_attack_speed = 0

        self.number_of_attacks = number_of_attacks
        self.current_number_of_attacks = 0

        self.shot_movement_speed = shot_movement_speed
        self.shot_factory = shot_factory
        self.position = spawn_position

    def update(self, delta_time):
        self.current_attack_speed += delta_time
    
    def draw(self, display):
        pass
    
    def shot(self):
        raise NotImplementedError
    
    def attack_finished(self):
        return self.current_number_of_attacks >= self.number_of_attacks
    
    def restart_attack(self):
        raise NotImplementedError