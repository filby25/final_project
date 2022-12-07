import pygame
import sys
from time import sleep
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

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((500,500))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen_rect = self.screen.get_rect()
        self.asteroids = pygame.sprite.Group(Asteroid(self.screen_rect.midleft),
                                             Asteroid(self.screen_rect.midtop),
                                             Asteroid(self.screen_rect.midright),
                                             Asteroid(self.screen_rect.midbottom)
                                             )
        self.ships = Ships(self.screen_rect.center)
        self.ship = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()
        self.space = pygame.image.load('images/blue.png')
        self.space_rect = self.space.get_rect()
        self.background = pygame.surface.Surface((self.screen_rect.width, self.screen_rect.height))
        self.missile_sound = pygame.mixer.Sound('sounds/missile_shot.ogg')
        self.asteroid_sound = pygame.mixer.Sound('sounds/asteroid_shot.ogg')
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
            if len(self.missiles) < settings.MISSILES_ALLOWED:
                self.ships.shooting = True
                pygame.mixer.Sound.play(self.missile_sound)


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
            level = 0
            self.check_events()
            if settings.SHIP_LIMIT > 0:
                level += 1
                self.ships.update(self.screen_rect.height, self.screen_rect.width, self.missiles)
                self.asteroids.update(self.screen_rect)
                while pygame.sprite.groupcollide(self.missiles, self.asteroids, True, True):
                    pygame.mixer.Sound.play(self.asteroid_sound)
                self.missiles.update()
                for missile in self.missiles.copy():
                    if missile.rect.bottom <= 0 or missile.rect.top >= self.screen_rect.bottom:
                        self.missiles.remove(missile)
                    if missile.rect.right <= 0 or missile.rect.left >= self.screen_rect.right:
                        self.missiles.remove(missile)
                if pygame.sprite.spritecollideany(self.ships, self.asteroids):
                    settings.SHIP_LIMIT -= 1
                    self.asteroids.empty()
                    self.missiles.empty()
                    self.ships.reset(self.screen)
                self.update_screen()
            # if self.asteroids.empty():
            #     level += 1
            #     for i range(level):
            #         self.asteroids.add(Asteroid((0,0)))
            clock.tick(60)

    def update_screen(self):
        """Update the screen and flip to new screen"""
        self.screen.blit(self.background, (0, 0))
        self.ships.blitme(self.screen)
        self.asteroids.draw(self.screen)
        for missile in self.missiles.sprites():
            missile.blitme(self.screen)
        pygame.display.flip()



if __name__ == '__main__':
    ag = AsteroidShooter()
    ag.run_game()