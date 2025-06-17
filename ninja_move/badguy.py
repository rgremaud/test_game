import pygame 
from pygame.sprite import Sprite

class Badguy(Sprite):
    """A class to represent the bad red ninjas!"""

    def __init__(self, the_game):
        """Initialize the red ninja and set starting position"""
        super().__init__()
        self.screen = the_game.screen
        self.settings = the_game.settings

        # Load the red ninja image and set its rect attribute.
        self.image = pygame.image.load('images/redninja.bmp')
        self.rect = self.image.get_rect()

        # Start each new badguy near the top right of the screen.
        self.rect.x = the_game.settings.screen_width - self.rect.width
        self.rect.y = self.rect.height

        # Store the badguy's exact vertical position.
        self.y = float(self.rect.y)
    
    def update(self):
        """Move badguy up and down"""
        self.y += self.settings.badguy_speed * self.settings.badguy_direction
        self.rect.y = self.y

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)
    
    
