import pygame


class Ships:
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

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up=False
        self.moving_down=False


    def update(self):
        """Update the ships rotation based on the movement flag"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed


        #update rect object form movement commands
        self.rect.x = self.x
        self.rect.y= self.y
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def move(self):
        """center the ship on the screen"""
        self.rect.center = self.image_center