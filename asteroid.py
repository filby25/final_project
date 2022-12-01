import pygame
from settings import Settings
from random import randint


class Asteroid:
    """A class to load in and control the asteroids"""

    def __init__(self, position):
        """Initialize the asteroids and put them in place"""
        self.settings = Settings()
        self.x_direction = 1
        self.y_direction = 1
        self.x_speed = self.settings.asteroid_speedx
        self.y_speed = self.settings.asteroid_speedy
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
            self.x_speed = randint(4, 5) * self.x_direction
        ### right wall
        if self.rect.right > screen_rect.width:
            # move to the left (flip X)
            self.x_direction *= -1
            self.rect.right = screen_rect.width
            self.x_speed = randint(4, 5) *self.x_direction
        ### top wall
        if self.rect.top <= 0:
            #move down (flip y)
            self.y_direction *= -1
            self.rect.top = 0
            self.y_speed = randint(4,5) * self.y_direction
        ### bottom wall
        if self.rect.bottom > screen_rect.height:
            #move up (flip y)
            self.y_direction *= -1
            self.rect.bottom= screen_rect.height
            self.y_speed = randint(4,5) * self.y_direction


        # if self.rect.right > screen_rect.right or self.rect.left < 0:
        #     self.settings.asteroid_direction *= -1
        #     self.settings.asteroid_speedx = randint(3, 6) * self.settings.asteroid_direction
        # if self.rect.top < screen_rect.top or self.rect.bottom > 720:
        #     self.settings.asteroid_direction *= -1
        #     self.settings.asteroid_speedy = randint(3, 6) * self.settings.asteroid_direction
        #
        # if self.rect_2.right > self.screen_rect.right or self.rect_2.left < self.screen_rect.left:
        #     self.settings.asteroid_direction_2 *= -1
        #     self.settings.asteroid_speedx_2 = randint(3, 6) * self.settings.asteroid_direction_2
        #
        # if self.rect_2.top < self.screen_rect.top or self.rect_2.bottom > self.screen_rect.bottom:
        #     self.settings.asteroid_direction_2 *= -1
        #     self.settings.asteroid_speedy_2 = randint(3, 6) * self.settings.asteroid_direction_2

        self.rect.left += self.x_speed
        self.rect.bottom += self.y_speed





    def blitme(self, screen):
        """Draw the new asteroid on the screen"""
        screen.blit(self.image, self.rect)
