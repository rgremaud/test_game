import pygame
from pygame.sprite import Sprite
import random

class Barrier(Sprite):
    """Generate randomly sized barriers to avoid hitting"""

    def __init__(self, race_day):
        """Initialize the barrier."""
        super().__init__()
        self.screen = race_day.screen
        self.settings = race_day.settings
        self.screen_rect = race_day.screen.get_rect()

        # Load the barrier image and get its rect
        self.top_image = pygame.image.load('images/barrier.bmp')
        self.top_rect = self.top_image.get_rect()

        self.bottom_image = pygame.image.load('images/barrier.bmp')
        self.bottom_rect = self.bottom_image.get_rect()
        
        # Start the rectangle at the top left
        self.top_rect.x, self.top_rect.y = 295, random.randint(-500, -325)
        self.bottom_rect.x, self.bottom_rect.y = 295, random.randint(325, 500)

        # Store a float for the barrier's exact x position
        self.top_x = float(self.top_rect.x)
        self.bottom_x = float(self.bottom_rect.x)
    
    def update(self):
        """Move the racecar down the screen"""
        self.top_x -= self.settings.barrier_speed
        self.top_rect.x = self.top_x
        self.bottom_x -= self.settings.barrier_speed
        self.bottom_rect.x = self.bottom_x

    def blitme(self):
        """Draw the barrier at its current location"""
        self.screen.blit(self.top_image, self.top_rect)
        self.screen.blit(self.bottom_image, self.bottom_rect)