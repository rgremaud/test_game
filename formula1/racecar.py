import pygame
from pygame.sprite import Sprite

class Racecar(Sprite):
    """A class to build a racecar"""

    def __init__(self, race_day):
        """Initialize the racecar."""
        super().__init__()
        self.screen = race_day.screen
        self.settings = race_day.settings
        self.screen_rect = race_day.screen.get_rect()

        # Load the racecar image and get its rect
        self.image = pygame.image.load('images/racecar.bmp')
        self.rect = self.image.get_rect()

        # Start the racecar at the middle of the screen
        self.rect.center = self.screen_rect.center

        # Store a float for the racecar's exact y position
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the racecar down the screen"""
        self.y += self.settings.racecar_speed
        self.rect.y = self.y

    def jump(self):
        """Jump the car up"""
        self.y -= self.settings.racecar_jump
        self.rect.y = self.y
        self.speed_increase()
    
    def speed_increase(self):
        """Increase the rate of car's speed"""
        self.settings.racecar_speed *= 1.05
        if self.settings.racecar_jump <= 75:
            self.settings.racecar_jump *= 1.05

    def blitme(self):
        """Draw the racecar at its current location"""
        self.screen.blit(self.image, self.rect)