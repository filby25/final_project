import pygame
from pygame.sprite import Sprite
from ships import Ships
import settings


class Missile(Sprite):
    """Class to manage missiles fired from the ship"""

    def __init__(self, ag_game):
        super().__init__()
        self.screen = ag_game.screen
        self.settings = ag_game.settings
        self.screen_rect = ag_game.screen.get_rect()
        self.ships=Ships(self)
        self.color = settings.MISSILE_COLOR
        self.rect = pygame.Rect(0,0, settings.MISSILE_WIDTH, settings.MISSILE_LENGTH)

        if self.ships == self.ships.moving_up:
            self.rect = pygame.Rect(0,0, settings.MISSILE_WIDTH, settings.MISSILE_LENGTH)
            self.rect.midtop = ag_game.ships.rect.midtop
        if self.ships == self.ships.moving_left:
            self.rect = pygame.Rect(0,0,settings.MISSILE_LENGTH, settings.MISSILE_WIDTH)
            self.rect.midleft = ag_game.ships.rect.midleft
        if self.ships == self.ships.moving_right:
            self.rect = pygame.Rect(0,0,settings.MISSILE_LENGTH, settings.MISSILE_WIDTH)
            self.rect.midright = ag_game.ships.rect.midright
        if self.ships == self.ships.moving_down:
            self.rect = pygame.Rect(0,0,settings.MISSILE_WIDTH, settings.MISSILE_LENGTH)
            self.rect.midbottom = ag_game.ships.rect.midbottom

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """function to update the missiles position"""
        if self.ships.moving_up:
            self.y -= settings.MISSILE_SPEED
        if self.ships.moving_down:
            self.y += settings.MISSILE_SPEED
        if self.ships.moving_right:
            self.x += settings.MISSILE_SPEED
        if self.ships.moving_left:
            self.x -= settings.MISSILE_SPEED
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_missile(self):
        """Draw the missile to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)