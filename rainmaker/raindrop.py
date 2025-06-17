import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to a single raindrop in the sky"""

    def __init__(self, rainmaker):
        """Initialize raindrops and set position"""
        super().__init__()
        self.screen = rainmaker.screen
        self.settings = rainmaker.settings

        # Load the raindrop image and set its rect
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the raindrop down the screen."""
        # Update the exact position of the rain
        self.y += self.settings.rain_speed

        # Update the rect position
        self.rect.y = self.y