
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
