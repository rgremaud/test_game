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
        self.image = pygame.image.load('images/barrier.bmp')
        self.rect = self.image.get_rect()
        
        # Start the rectangle at the top left
        self.rect.x, self.rect.y = 295, random.randint(-500, -325)

    def blitme(self):
        """Draw the barrier at its current location"""
        self.screen.blit(self.image, self.rect)