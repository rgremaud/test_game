import pygame 
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to manage ninja star fired by ninja."""

    def __init__(self, the_game):
        """Create a ninja star object at the ship's current position."""
        super().__init__()
        self.screen = the_game.screen
        self.settings = the_game.settings
        self.color = self.settings.star_color

        # Create a ninja star at (0, 0) then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.star_width, 
                                self.settings.star_height)
        self.rect.midright = the_game.ninja.rect.midright # may need to correct to midtop

        # Store the ninja star position as a float.
        self.x = float(self.rect.x)

    def update(self):
        """Move the ninja star across the screen"""
        # Update the exact position of the ninja star.
        self.x += self.settings.ninja_speed
        # Update the rect position
        self.rect.x = self.x

    def draw_star(self):
        """Draw the ninja star to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)