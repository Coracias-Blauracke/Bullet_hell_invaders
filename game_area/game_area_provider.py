from game_area.attacks.attack_factory import AttackFactory
from game_area.point_factory import PointFactory
from game_area.shots.shot_factory import ShotFactory
from providers.provider import Provider


class GameAreaProvider(Provider):

    def __init__(self, register, resolve):
        super().__init__(register, resolve)

    def register_services(self):
        self.register('point_factory', lambda: PointFactory())
        self.register('shot_factory', lambda: ShotFactory(
            point_factory=self.resolve('point_factory')
        ))
        self.register('attack_factory', lambda: AttackFactory(
            shot_factory=self.resolve('shot_factory'),
            game_controller=self.resolve('game_controller')
        ))

    def run_services(self):
        pass