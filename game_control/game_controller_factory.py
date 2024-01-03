from game_control.game_controller import GameController


class GameControllerFactory:
    
    def create_game_controller(self):
        return GameController()