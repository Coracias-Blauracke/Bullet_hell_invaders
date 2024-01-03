import math
from game_area.attacks.attack import Attack


class CircularAttack(Attack):
    
    def __init__(
            self, 
            attack_speed,
            number_of_attacks,
            number_of_shots,
            shot_movement_speed,
            spawn_position,
            shot_factory,
            game_controller):
        super().__init__(attack_speed, number_of_attacks, shot_movement_speed, spawn_position, shot_factory)
        self.number_of_shots = number_of_shots
        self.game_controller = game_controller

    def update(self, delta_time):
        super().update(delta_time)
        if self.current_attack_speed >= self.attack_speed and not self.attack_finished():
            self.current_attack_speed -= self.attack_speed
            self.current_number_of_attacks += 1
            self.shot()
        
    def shot(self):
        for i in range(self.number_of_shots):
            shot_angle = 2 * math.pi / self.number_of_shots * i
            new_shot = self.shot_factory.create_simple_shot(
                self.position,
                movement_speed = self.shot_movement_speed,
                angle = shot_angle)
            self.game_controller.add_object(new_shot)
    
    def attack_finished(self):
        return self.current_number_of_attacks >= self.number_of_attacks
    
    def restart_attack(self):
        self.current_attack_speed = 0
        self.current_number_of_attacks = 0