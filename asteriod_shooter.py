import pygame
import sys
from settings import Settings
from ships import Ships
import time
from asteroid import Asteroid

class AsteroidShooter:
    """Overall class to manage the game as a whole"""

    def __init__(self):
        """Initialize the game and create game resources"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((500,500))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.asteroid = Asteroid((0,400))
        self.ships = Ships(self)

        self.space = pygame.image.load('images/blue.png')
        self.screen_rect = self.screen.get_rect()
        self.space_rect = self.space.get_rect()
        self.background = pygame.surface.Surface((self.screen_rect.width, self.screen_rect.height))
        for y in range(self.screen_rect.height):
            for x in range(self.screen_rect.width):
                self.background.blit(self.space, (x * self.space_rect.width, y * self.space_rect.height))
        print(self.screen_rect)

    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_a:
            self.ships.moving_left=True
            self.ships.image = pygame.image.load('images/player_left.png')
        if event.key == pygame.K_d:
            self.ships.moving_right=True
            self.ships.image= pygame.image.load('images/player_right.png')
        if event.key == pygame.K_w:
            self.ships.moving_up=True
            self.ships.image= pygame.image.load('images/player.png')
        if event.key == pygame.K_s:
            self.ships.moving_down=True
            self.ships.image= pygame.image.load('images/player_down.png')

    def _check_asteroid_collisions(self):
        """Check for collisions"""
        #collisions = pygame.Rect.collidelistall()
    def _check_keyup_events(self,event):
        """Respond to key releases"""
        if event.key == pygame.K_a:
            self.ships.moving_left=False
        elif event.key == pygame.K_d:
            self.ships.moving_right=False
        elif event.key == pygame.K_w:
            self.ships.moving_up=False
        elif event.key == pygame.K_s:
            self.ships.moving_down=False


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def run_game(self):
        """Start the main loop for the game"""
        clock= pygame.time.Clock()
        while True:
            self._check_events()
            self.ships.update()
            self.asteroid.update(self.screen_rect)
            self._check_asteroid_collisions()
            self._update_screen()
            clock.tick(60)

    def _update_screen(self):
        """Update the screen and flip to new screen"""
        self.screen.blit(self.background, (0, 0))
        self.ships.blitme()
        self.asteroid.blitme(self.screen)
        pygame.display.flip()



if __name__ == '__main__':
    ag = AsteroidShooter()
    ag.run_game()