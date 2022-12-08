import pygame
from missiles import Missile
from pygame.sprite import Sprite
import settings
class Station(Sprite):
    """A class to create and manage the ship"""

    def __init__(self, position):
        """Initialize the ship and put it in its starting position"""
        super().__init__()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/station.png')
        self.rect = self.image.get_rect()

        self.rect.center = position

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up=False
        self.moving_down=False

    def update(self, max_height, max_width):
        """Update the ships rotation based on the movement flag"""

        if self.moving_right and self.rect.right < max_width:
            self.rect.x += settings.SHIP_SPEED+3
        if self.rect.left > 0 and self.moving_left:
            self.rect.x -= settings.SHIP_SPEED+3
        if self.moving_up and self.rect.top > 0 :
            self.rect.y -= settings.SHIP_SPEED+3
        if self.moving_down and self.rect.bottom < max_height:
            self.rect.y += settings.SHIP_SPEED+3
    def blitme(self, screen):
        """draw the ship at its current location"""
        screen.blit(self.image, self.rect)

    def reset(self, screen):
        """reset the ship to the center of the screen"""
        self.rect.center = screen.get_rect().center