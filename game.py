import sys

import pygame

from settings import Settings
from ninja import Ninja

class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("The Game")
        self.ninja = Ninja(self)

    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ninja.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ninja.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ninja.moving_left = True
        elif event.key == pygame.K_UP:
            self.ninja.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ninja.moving_down = True
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ninja.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ninja.moving_left = False
        elif event.key == pygame.K_UP:
            self.ninja.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ninja.moving_down = False

    def _update_screen(self):
         """Updates images on the screen, and flip to the new screen."""
         self.screen.fill(self.settings.bg_color)
         self.ninja.blitme()

         pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance and run the game.
    the_game = Game()
    the_game.run_game()