class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        # Screen settings
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (68, 32, 140)

        # Ninja settings
        self.ninja_speed = 3

        # Ninja star settings
        self.star_speed = 3.0
        self.star_width = 15
        self.star_height = 15
        self.star_color = (200, 200, 200)