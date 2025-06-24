class Settings:
    """A class to store settings for race day."""

    def __init__(self):
        # Screen settings
        self.screen_width = 320
        self.screen_height = 569
        self.bg_color = (250, 250, 250)

        self.speedup_scale = 1.05

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Racecar Settings
        self.racecar_gravity = .5
        self.racecar_jump = 50

        # Barrier Settings
        self.barrier_speed = .5
    
    def increase_speed(self):
        """Increase speed settings"""
        self.racecar_gravity *= self.speedup_scale
        if self.racecar_jump <= 75:
            self.racecar_jump *= self.speedup_scale