import pygame


class Planet:
    def __init__(self, mass, radius, x, y, vx=0, vy=0, color=(255, 255, 255)):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (100, 100), 30)
