import pygame
from pygame.colordict import THECOLORS
from game_area.game_area_provider import GameAreaProvider
from game_area.point import Point
from game_control.game_control_provider import GameControlProvider
from providers.provider_registry import ProviderRegistry
from providers.service_state_factory import ServiceStateFactory


if __name__ == '__main__':

    service_state_factory = ServiceStateFactory()
    provider_registry = ProviderRegistry(service_state_factory)
    provider_registry.register_providers([
        lambda register, resolve: GameAreaProvider(register, resolve),
        lambda register, resolve: GameControlProvider(register, resolve)
    ])
    provider_registry.run_providers()
    attack_factory = provider_registry.get_service('attack_factory')
    attack = attack_factory.create_example_attack(Point(250, 250))
    game_controller = provider_registry.get_service('game_controller')
    game_controller.add_object(attack)

    width = 500
    height = 500
    pygame.init()
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Bullet hell')
    clock = pygame.time.Clock()


    while True:
        display.fill(THECOLORS['white'])
        delta_time = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key is pygame.K_q:
                pygame.quit()
                quit()

        game_controller.update(delta_time)
        game_controller.draw(display)

        pygame.display.update()