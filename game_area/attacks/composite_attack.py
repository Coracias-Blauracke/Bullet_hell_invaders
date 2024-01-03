from game_area.attacks.attack import Attack


class CompositeAttack(Attack):

    def __init__(
            self,
            attacks,
            attack_speed,
            number_of_attacks,
            shot_movement_speed,
            spawn_position,
            shot_factory):
        super().__init__(spawn_position, attack_speed, shot_movement_speed, number_of_attacks, shot_factory)
        self.attacks = attacks
        self.current_attack = 0

    def update(self, delta_time):
        if self.attack_finished():
            return
        
        self.attacks[self.current_attack].update(delta_time)
        if self.attacks[self.current_attack].attack_finished():
            self.current_attack += 1
        
    def draw(self, display):
        pass

    def attack_finished(self):
        return self.current_attack >= len(self.attacks)
    
    def restart_attack(self):
        self.current_attack = 0
        for attack in self.attacks:
            attack.restart_attack()