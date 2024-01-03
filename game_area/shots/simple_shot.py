import pygame
import math

from pygame.colordict import THECOLORS
from game_area.shots.shot import Shot




class SimpleShot(Shot):

    def __init__(self, position, movement_speed, radius, angle, color):
        super().__init__(position, movement_speed, radius, angle)
        self.color = color

    def update(self, delta_time):
        self.position.x += self.movement_speed * delta_time * math.cos(self.angle)
        self.position.y += self.movement_speed * delta_time * math.sin(self.angle)

    def draw(self, display):
        pygame.draw.circle(display, THECOLORS[self.color], (self.position.x, self.position.y), self.radius)