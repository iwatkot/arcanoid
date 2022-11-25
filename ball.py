import pygame


class Ball:
    def __init__(self, ag):
        pygame.init()
        self.screen = ag.screen
        self.screen_rect = ag.screen_rect
        self.settings = ag.settings
        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = ag.arkanoid.rect.midtop
        self.rect.y -= 3
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.moving = False
        self.x_direction = 1
        self.y_direction = -1

    def launch(self):
        self.moving = True

    def update(self):
        if self.moving:
            self.x += self.settings.ball_speed * self.x_direction
            self.y += self.settings.ball_speed * self.y_direction
            self.rect.x = self.x
            self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_me(self, ag):
        self.rect.midbottom = ag.arkanoid.rect.midtop
        self.rect.y -= 3
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
