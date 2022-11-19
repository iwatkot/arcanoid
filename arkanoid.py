import pygame

class Arkanoid:
    def __init__(self, ag):
        #pygame.init()
        self.screen = ag.screen
        self.screen_rect = ag.screen_rect
        self.settings = ag.settings
        self.image = pygame.image.load("images/arcanoid.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.arcanoid_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.arcanoid_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_me(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)