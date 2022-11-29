import pygame


class Ship:
    """A class to create and manage the ship"""

    def __init__(self, ag_game):
        """Initialize the ship and put it in its starting position"""
        self.screen = ag_game.screen
        self.settings = ag_game.settings
        self.screen_rect = ag_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.image_center = self.rect.center

        # movement flag
        self.turning_right = False
        self.turning_left = False

    def rotate_image(self):

        rotated_image = pygame.transform.rotate(self.image, self.settings.rotation_speed)
        new_rect = rotated_image.get_rect(center=self.image_center)

        return rotated_image, new_rect
    def update(self):
        """Update the ships rotation based on the movement flag"""

        if self.turning_right:
            self.image= self.rotate_image()
            #self.image = pygame.transform.rotate(self.image, -self.settings.rotation_speed)
        if self.turning_left:
            self.image= self.rotate_image()
            #self.image = pygame.transform.rotate(self.image, self.settings.rotation_speed)

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rotate_image)

    def move(self):
        """center the ship on the screen"""
        self.rect.center = self.coordinate
