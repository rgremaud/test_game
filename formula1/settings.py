class Settings:
    """A class to store settings for race day."""

    def __init__(self):
        # Screen settings
        self.screen_width = 320
        self.screen_height = 569
        self.bg_color = (250, 250, 250)

        # Racecar Settings
        self.racecar_speed = .5
        self.racecar_jump = 50