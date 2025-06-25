import pygame
from pygame.sprite import Sprite
import random

class Barrier(Sprite):
    """Generate randomly sized barriers to avoid hitting"""

    def __init__(self, race_day, type):
        """Initialize the barrier."""
        super().__init__()
        self.screen = race_day.screen
        self.settings = race_day.settings
        self.screen_rect = race_day.screen.get_rect()

        self.type = type

        # Load the barrier image and get its rect
        self.image = pygame.image.load('images/barrier.bmp')
        self.rect = self.image.get_rect()
        
        # Check if top or bottom barrier
        if self.type == 'top':
            self.rect.x, self.rect.y = 295, random.randint(-500, -325)
            
        if self.type == 'bottom':
            self.rect.x, self.rect.y = 295, random.randint(325, 500)
        
        self.x = float(self.rect.x)
       

    
    def update(self):
        """Move the racecar down the screen"""
        self.x -= self.settings.barrier_speed
        self.rect.x = self.x
        #self.bottom_x -= self.settings.barrier_speed
        #self.bottom_rect.x = self.bottom_x

    def blitme(self):
        """Draw the barrier at its current location"""
        self.screen.blit(self.image, self.top_rect)
        #self.screen.blit(self.bottom_image, self.bottom_rect)