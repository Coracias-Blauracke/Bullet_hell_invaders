from game_control.game_controller_factory import GameControllerFactory
from providers.provider import Provider


class GameControlProvider(Provider):

    def __init__(self, register, resolve):
        super().__init__(register, resolve)

    def register_services(self):
        self.register('game_controller_facory', lambda: GameControllerFactory())
        self.register('game_controller', lambda: self.resolve('game_controller_facory').create_game_controller())

    def run_services(self):
        pass

