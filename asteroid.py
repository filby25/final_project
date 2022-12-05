import pygame

import settings
from settings import Settings
from random import randint, random
from pygame.sprite import Sprite

class Asteroid(Sprite):
    """A class to load in and control the asteroids"""

    def __init__(self, position):
        """Initialize the asteroids and put them in place"""
        super().__init__()
        self.x_direction = 1
        self.y_direction = 1
        self.x_speed = 4.5
        self.y_speed = 4.5
        self.image = pygame.image.load('images/asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self, screen_rect):
        """Update the asteroid based on movement"""

        ### left wall
        if self.rect.left <= 0:
           # move to the right (flip X)
            self.x_direction *= -1
            self.rect.left = 0
            self.x_speed = (settings.MIN_ASTEROID_SPEED+random()*settings.RANGE_ASTEROID_SPEED) * self.x_direction
        ### right wall
        if self.rect.right > screen_rect.width:
            # move to the left (flip X)
            self.x_direction *= -1
            self.rect.right = screen_rect.width
            self.x_speed = (settings.MIN_ASTEROID_SPEED+random()*settings.RANGE_ASTEROID_SPEED) * self.x_direction
        ### top wall
        if self.rect.top <= 0:
            #move down (flip y)
            self.y_direction *= -1
            self.rect.top = 0
            self.y_speed = (settings.MIN_ASTEROID_SPEED+random()*settings.RANGE_ASTEROID_SPEED) * self.y_direction
        ### bottom wall
        if self.rect.bottom > screen_rect.height:
            #move up (flip y)
            self.y_direction *= -1
            self.rect.bottom= screen_rect.height
            self.y_speed = (settings.MIN_ASTEROID_SPEED+random()*settings.RANGE_ASTEROID_SPEED) * self.y_direction

        self.rect.left += self.x_speed
        self.rect.bottom += self.y_speed


