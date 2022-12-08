import pygame
import sys
from time import sleep
from random import choice
import settings
from ships import Ships
from station import Station
from asteroid import Asteroid

class AsteroidShooter:
    """Overall class to manage the game as a whole"""

    def __init__(self):
        """Initialize the game and create game resources"""

        pygame.font.init()
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((500,500))
        self.screen_rect = self.screen.get_rect()
        self.rand_side = (self.screen_rect.topleft, self.screen_rect.topright, self.screen_rect.bottomleft, self.screen_rect.bottomright, self.screen_rect.midtop, self.screen_rect.midright, self.screen_rect.midbottom, self.screen_rect.midleft)
        self.asteroids = pygame.sprite.Group()
        self.stations= Station(self.screen_rect.center)
        self.station= pygame.sprite.Group()
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
        #station controls
        if event.key == pygame.K_UP:
            self.stations.moving_up = True
            self.stations.image = pygame.image.load('images/station.png')
        if event.key == pygame.K_DOWN:
            self.stations.moving_down = True
            self.stations.image = pygame.image.load('images/station_down.png')
        if event.key == pygame.K_LEFT:
            self.stations.moving_left = True
            self.stations.image = pygame.image.load('images/station_left.png')
        if event.key == pygame.K_RIGHT:
            self.stations.moving_right = True
            self.stations.image = pygame.image.load('images/station_right.png')
        # ship controls
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
        if event.key == pygame.K_UP:
            self.stations.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.stations.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.stations.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.stations.moving_right = False
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
        font_lose = pygame.font.SysFont('comicsans.ttf', 70)
        font = pygame.font.SysFont('comicsansms.ttf', 50)
        text_lose = font_lose.render('YOU LOSE', 1, (0,0,0))
        text = font.render('Level:  ', True, (30,30,30))

        level = 1
        while True:
            self.check_events()

            if settings.SHIP_LIMIT == 0:
                self.screen.fill((255,255,255))
                self.screen.blit(text_lose, (520, 300))
                pygame.display.update()
                sleep(2)
                sys.exit()


            if settings.SHIP_LIMIT > 0:
                if len(self.asteroids) == 0:
                    for i in range(level):
                        self.asteroids.add(Asteroid(choice(self.rand_side)))
                    level += 1
                #updates the ship, asteroids, and missiles
                self.screen.blit(text, text.get_rect())
                self.ships.update(self.screen_rect.height, self.screen_rect.width, self.missiles)
                self.asteroids.update(self.screen_rect)
                self.missiles.update()
                self.stations.update(self.screen_rect.height, self.screen_rect.width)
                #plays a sound when an asteroid gets hit
                while pygame.sprite.groupcollide(self.missiles, self.asteroids, True, True):
                    pygame.mixer.Sound.play(self.asteroid_sound)
                #remove the missile if it goes off screen
                for missile in self.missiles.copy():
                    if missile.rect.bottom <= 0 or missile.rect.top >= self.screen_rect.bottom:
                        self.missiles.remove(missile)
                    if missile.rect.right <= 0 or missile.rect.left >= self.screen_rect.right:
                        self.missiles.remove(missile)
                #resets the position of the ship and asteroids when the ship gets hit
                if pygame.sprite.spritecollideany(self.ships, self.asteroids) or pygame.sprite.spritecollideany(self.stations, self.asteroids) or pygame.sprite.spritecollideany(self.stations, self.missiles):
                    settings.SHIP_LIMIT -= 1
                    self.asteroids.empty()
                    self.missiles.empty()
                    self.stations.reset(self.screen)
                    self.ships.reset(self.screen)
                    level = level-1
                self.update_screen()
                clock.tick(60)
            else:
                sleep(5)
                sys.exit()

    def update_screen(self):
        """Update the screen and flip to new screen"""
        self.screen.blit(self.background, (0, 0))
        self.stations.blitme(self.screen)
        self.ships.blitme(self.screen)
        self.asteroids.draw(self.screen)
        for missile in self.missiles.sprites():
            missile.blitme(self.screen)
        pygame.display.flip()



if __name__ == '__main__':
    ag = AsteroidShooter()
    ag.run_game()