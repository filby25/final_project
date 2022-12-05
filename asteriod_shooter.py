import pygame
import sys

import settings
from settings import Settings
from ships import Ships
from missiles import Missile
from asteroid import Asteroid

class AsteroidShooter:
    """Overall class to manage the game as a whole"""

    def __init__(self):
        """Initialize the game and create game resources"""

        pygame.init()
        self.settings = Settings()

        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((500,500))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen_rect = self.screen.get_rect()
        self.asteroids = pygame.sprite.Group(Asteroid((self.screen_rect.midleft)),
                                             Asteroid((self.screen_rect.midtop)),
                                             Asteroid((self.screen_rect.midright)),
                                             Asteroid((self.screen_rect.midbottom))
                                             )
        self.ships = Ships(self)
        self.missiles= Missile(self)
        self.ship = pygame.sprite.Group()
        self.missile = pygame.sprite.Group()

        self.space = pygame.image.load('images/blue.png')
        self.space_rect = self.space.get_rect()
        self.background = pygame.surface.Surface((self.screen_rect.width, self.screen_rect.height))
        for y in range(self.screen_rect.height):
            for x in range(self.screen_rect.width):
                self.background.blit(self.space, (x * self.space_rect.width, y * self.space_rect.height))

    def check_keydown_events(self, event):
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
        if event.key == pygame.K_SPACE:
            self.missiles.update()

    def collisions(self):
        """Check collisions"""
        if pygame.sprite.spritecollideany(self.ships, self.asteroids):
            pygame.sprite.Group.remove(self.asteroids)
            print("collision")
            self.restart_level()

    def restart_level(self):
        """restart level if the ship gets hit"""
        if settings.SHIP_LIMIT > 0:
            self.ships.move()



    # def end_game(self):
    #     """function to end the game"""
    #     if settings.SHIP_LIMIT == 0:
    #         sys.exit()

    def check_keyup_events(self,event):
        """Respond to key releases"""
        if event.key == pygame.K_a:
            self.ships.moving_left=False
        elif event.key == pygame.K_d:
            self.ships.moving_right=False
        elif event.key == pygame.K_w:
            self.ships.moving_up=False
        elif event.key == pygame.K_s:
            self.ships.moving_down=False


    def check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def run_game(self):
        """Start the main loop for the game"""
        clock= pygame.time.Clock()
        while True:
            self.check_events()
            self.ships.update()
            self.collisions()
            self.asteroids.update(self.screen_rect)
            self.asteroids.update(self.screen_rect)
            #self.collisions()
            # if self.asteroids.empty():
            #     level += 1
            #     for i range(level):
            #         self.asteroids.add(Asteroid((0,0)))
            self.update_screen()
            clock.tick(60)

    def update_screen(self):
        """Update the screen and flip to new screen"""
        self.screen.blit(self.background, (0, 0))
        self.ships.blitme()
        self.asteroids.draw(self.screen)
        self.missile.draw(self.screen)
        pygame.display.flip()



if __name__ == '__main__':
    ag = AsteroidShooter()
    ag.run_game()