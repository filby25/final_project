SHIP_SPEED = 4
MIN_ASTEROID_SPEED= 3.5
RANGE_ASTEROID_SPEED= 1.5
SHIP_LIMIT = 3
MISSILE_SPEED = 8
MISSILES_ALLOWED = 24

class Settings:
    """A place to store settings for asteroid shooter"""


    def __init__(self):
        """Initialize the game's settings"""

        #ship settings
        self.rotation_speed=2
        self.ship_limit=2
        self.ship_speed = 2

        #missile settings
        self.missile_speed=1.2
        self.missile_width=1.5
        self.missile_height=7
        self.missile_color=(244,252,3)
        self.missile_allowed=7

        #asteroid settings
        self.asteroid_speedy = 4.5
        self.asteroid_speedx = 4.5
        self.asteroid_direction = 1
        self.asteroid_speedy_2 = 4.5
        self.asteroid_speedx_2 = 4.5
        self.asteroid_direction_2 = 1

