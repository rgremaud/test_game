import pygame
from pygame.sprite import Sprite

class Background:
    """Generate a background image for game"""
    def __init__(self, race_day):
        """Draw background image"""
        super().__init__()
        self.screen = race_day.screen
        self.settings = race_day.settings
        self.screen_rect = race_day.screen.get_rect()

        # Load background image and get its rect.
        self.image = pygame.image.load('images/road.bmp')
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = 0, 0

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)