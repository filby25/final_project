import pygame
from pygame.sprite import Sprite
import settings


class Missile(Sprite):
    """Class to manage missiles fired from the ship"""

    def __init__(self, direction, position):
        super().__init__()
        self.color = (184,222,60)
        if direction == 'up' or direction == 'down':
            self.image = pygame.surface.Surface((4,20))
        if direction == 'left' or direction == 'right':
            self.image = pygame.surface.Surface((20,4))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.image.fill(self.color)
        self.direction = direction

    def update(self):
        """function to shoot"""
        if self.direction == 'up':
            self.rect.y -= settings.MISSILE_SPEED
        if self.direction == 'down':
            self.rect.y += settings.MISSILE_SPEED
        if self.direction == 'left':
            self.rect.x -= settings.MISSILE_SPEED
        if self.direction == 'right':
            self.rect.x += settings.MISSILE_SPEED

    def blitme(self, screen):
        """Draw the missile to the screen"""
        screen.blit(self.image, self.rect)
