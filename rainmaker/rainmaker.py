import sys

import pygame

from settings import Settings
from rainman import Rainman
from raindrop import Raindrop
from random import randint

class Rainmaker:
    """Mini-game with the objective of catching rain."""

    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                              self.settings.screen_height))
        pygame.display.set_caption("Rainmaker")
        self.rainman = Rainman(self)
        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rainman.update()
            self._update_rain()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rainman.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rainman.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rainman.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rainman.moving_left = False

    def _create_rain(self):
        """Create a row of raindrops"""
        # Create a raindrop and add until row is filled
        # Add semi random gap between raindrops
        raindrop = Raindrop(self)
        raindrop_width = raindrop.rect.width

        current_x = raindrop_width
        while len(self.raindrops) <= randint(0,3):
            new_raindrop = Raindrop(self)
            new_raindrop.x = current_x
            new_raindrop.rect.x = current_x
            self.raindrops.add(new_raindrop)
            current_x += 2 * raindrop_width

    def _update_rain(self):
        """Summon a new row of rain when current one disapears"""
        self.raindrops.update()

        # Get rid of row of raindrops when they have disappeared.
        for raindrop in self.raindrops.copy():
            if raindrop.rect.bottom >= self.settings.screen_height:
                self.raindrops.remove(raindrop)
                self._create_rain()

    def _update_screen(self):
        """Update images on the screen and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rainman.blitme()
        self.raindrops.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance and run the game.
    rainmaker = Rainmaker()
    rainmaker.run_game()