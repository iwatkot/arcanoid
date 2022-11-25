import sys

import pygame

from time import sleep

from settings import Settings
from arkanoid import Arkanoid
from ball import Ball
from brick import Brick
from game_stats import GameStats


class ArkanoidGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode(self.settings.screen_resolution)
        pygame.display.set_caption("Arcanoid Game")
        self.screen_rect = self.screen.get_rect()
        self.arkanoid = Arkanoid(self)
        self.ball = Ball(self)
        self.bricks = pygame.sprite.Group()
        self._create_wall()

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.arkanoid.update()
                self._update_bricks()
                self._update_ball()
                self._check_ball_screen_edges()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_LEFT:
            self.arkanoid.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.arkanoid.moving_right = True
        elif event.key == pygame.K_SPACE:
            self.ball.launch()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.arkanoid.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.arkanoid.moving_right = False

    def _update_bricks(self):
        if pygame.sprite.spritecollideany(self.ball, self.bricks):
            hitted_brick = pygame.sprite.spritecollideany(self.ball,
                                                          self.bricks)
            self._change_ball_direction(hitted_brick)
            self.bricks.remove(hitted_brick)

    def _change_ball_direction(self, hitted_brick):
        if (self.ball.rect.top - 2 < hitted_brick.rect.bottom <
            self.ball.rect.top + 2 or self.ball.rect.bottom - 2 <
                hitted_brick.rect.top < self.ball.rect.bottom + 2):
            self.ball.y_direction *= -1
        elif (self.ball.rect.right - 2 < hitted_brick.rect.left <
              self.ball.rect.right + 2 or self.ball.rect.left - 2 <
                hitted_brick.rect.right < self.ball.rect.left + 2):
            self.ball.x_direction *= -1

    def _check_ball_screen_edges(self):
        if (self.ball.rect.right >= self.screen_rect.right or
                self.ball.rect.left <= self.screen_rect.left):
            self.ball.x_direction *= -1
        if self.ball.rect.top <= self.screen_rect.top:
            self.ball.y_direction *= -1
        if (self.arkanoid.rect.top - 2 < self.ball.rect.bottom <
            self.arkanoid.rect.top + 2 and
                (self.arkanoid.rect.left < self.ball.rect.right and
                    self.arkanoid.rect.right > self.ball.rect.left)):
            self.ball.y_direction *= -1

    def _update_ball(self):
        self.ball.update()
        if self.ball.rect.bottom >= self.screen_rect.bottom:
            self._ball_out()

    def _ball_out(self):
        if self.stats.lives_left > 0:
            sleep(1)
            self.stats.lives_left -= 1
            self.ball.moving = False
            self.ball.x_direction = 1
            self.ball.y_direction = -1
            self.arkanoid.center_me()
            self.ball.center_me(self)
        else:
            self.stats.game_active = False

    def _create_wall(self):
        brick = Brick(self)
        brick_width, brick_height = brick.rect.size
        number_of_bricks = (self.screen_rect.width -
                            2 * brick_width) // (2 * brick_width)
        number_of_rows = (self.screen_rect.height // 2) // (2 * brick_height)
        for row_number in range(number_of_rows):
            for brick_number in range(number_of_bricks):
                self._create_brick(row_number, brick_number)

    def _create_brick(self, row_number, brick_number):
        brick = Brick(self)
        brick_width, brick_height = brick.rect.size
        brick.y = brick_height + 2 * brick_height * row_number
        brick.rect.y = brick.y
        brick.rect.x = brick_width + 2 * brick_width * brick_number
        self.bricks.add(brick)

    def _update_screen(self):
        self.screen.fill(self.settings.screen_background_color)
        self.arkanoid.blitme()
        self.ball.blitme()
        self.bricks.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    ag = ArkanoidGame()
    ag.run_game()
