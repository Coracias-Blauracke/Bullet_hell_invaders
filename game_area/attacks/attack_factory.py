import math
from game_area.attacks.circular_attack import CircularAttack
from game_area.attacks.composite_attack import CompositeAttack
from game_area.attacks.cone_rainbow_attack import ConeRainbowAttack


class AttackFactory:

    def __init__(self, shot_factory, game_controller):
        self.shot_factory = shot_factory
        self.game_controller = game_controller

    def create_small_circle_attack(self, attack_speed, shot_movement_speed, spawn_position):
        return CircularAttack(
            attack_speed,
            3,
            3,
            shot_movement_speed,
            spawn_position,
            self.shot_factory,
            self.game_controller)
    
    def create_medium_circle_attack(self, attack_speed, shot_movement_speed, spawn_position):
        return CircularAttack(
            attack_speed,
            5,
            20,
            shot_movement_speed,
            spawn_position,
            self.shot_factory,
            self.game_controller)
    
    def create_large_circle_attack(self, attack_speed, shot_movement_speed, spawn_position):
        return CircularAttack(
            attack_speed,
            5,
            100,
            shot_movement_speed,
            spawn_position,
            self.shot_factory,
            self.game_controller)
    
    def create_cone_rainbow_attack(self, attack_speed, shot_movement_speed, starting_angle, ending_angle, spawn_position):
        return ConeRainbowAttack(
            attack_speed,
            0,
            starting_angle,
            ending_angle,
            0.1,
            shot_movement_speed,
            spawn_position,
            self.shot_factory,
            self.game_controller)
    
    def create_example_attack(self, spawn_position):
        attack = lambda:  CompositeAttack([
                self.create_cone_rainbow_attack(0.01, 200, 0, math.pi * 2, spawn_position),
                self.create_cone_rainbow_attack(0.01, 200, math.pi * 2, 0, spawn_position)
            ],
            0,
            0,
            0,
            spawn_position,
            None)
        
        attack2 = lambda: CompositeAttack([
                attack(),
                attack()
            ],
            0,
            0,
            0,
            spawn_position,
            None)
        
        return CompositeAttack([
                attack2(),
                attack2()
            ],
            0,
            0,
            0,
            spawn_position,
            None)
        

        