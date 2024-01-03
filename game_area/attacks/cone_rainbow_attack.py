import math
from pygame.colordict import THECOLORS
from game_area.attacks.attack import Attack


class ConeRainbowAttack(Attack):

    def __init__(
            self, 
            attack_speed,
            number_of_attacks,
            starting_angle,
            ending_angle,
            shot_per_angle_change,
            shot_movement_speed,
            spawn_position,
            shot_factory,
            game_controller):
        super().__init__(attack_speed, number_of_attacks, shot_movement_speed, spawn_position, shot_factory)
        self.starting_angle = starting_angle
        self.ending_angle = ending_angle
        self.shot_per_angle_change = shot_per_angle_change
        self.current_angle = self.starting_angle
        self.game_controller = game_controller
        self.shot_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet']

    def update(self, delta_time):
        super().update(delta_time)
        if self.current_attack_speed >= self.attack_speed and not self.attack_finished():
            self.current_attack_speed -= self.attack_speed
            self.current_number_of_attacks += 1
            self.shot()
        
    def shot(self):
        new_shot = self.shot_factory.create_simple_shot(
            self.position,
            movement_speed = self.shot_movement_speed,
            angle = self.current_angle,
            color = self.shot_colors[self.current_number_of_attacks % len(self.shot_colors)]
            )
        self.game_controller.add_object(new_shot)
        if self.starting_angle < self.ending_angle:
            self.current_angle += self.shot_per_angle_change
        else:
            self.current_angle -= self.shot_per_angle_change

    def attack_finished(self):
        if self.starting_angle < self.ending_angle:
            return self.current_angle >= self.ending_angle
        return self.current_angle <= self.ending_angle
    
    def restart_attack(self):
        self.current_attack_speed = 0
        self.current_number_of_attacks = 0
        self.current_angle = self.starting_angle
