import pygame

from pygame.sprite import Sprite


class Brick(Sprite):
    def __init__(self, ag):
        super().__init__()
        self.settings = ag.settings
        self.screen = ag.screen
        self.screen_rect = ag.screen_rect
        self.image = pygame.image.load("images/brick.png")
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)
