import sys

import pygame

from settings import Settings
from ninja import Ninja
from ninja_star import Star
from sky_star import Skystar
from random import randint

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
        self.stars = pygame.sprite.Group()
        self.skystars = pygame.sprite.Group()

        self._create_sky()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ninja.update()
            self._update_stars()
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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_star()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ninja.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ninja.moving_left = False
        elif event.key == pygame.K_UP:
            self.ninja.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ninja.moving_down = False

    def _create_sky(self):
        """Create a night sky."""
        # Create a star and keep adding until no room is left.
        # Spacing between star is two star width
        skystar = Skystar(self)
        skystar_width, skystar_height = skystar.rect.size

        current_x, current_y= skystar_width * 2, skystar_height * 2
        while current_y < (self.settings.screen_height - 15 * skystar_height):
            while current_x < (self.settings.screen_width - 2 * skystar_width):
                self._create_skystar(current_x, current_y)
                current_x += randint(30, 40)
            # Finished a row; reset x value and increment y value.
            current_x = skystar_width * 2
            current_y += randint(40, 60)
    
    def _create_skystar(self, x_position, y_position):
        """Create a skystar and place it in the row."""
        new_skystar = Skystar(self)
        new_skystar.x = x_position
        new_skystar.rect.x = x_position
        new_skystar.rect.y = y_position
        self.skystars.add(new_skystar)
    
    def _fire_star(self):
        """Create a new star and add it to the star group."""
        new_star = Star(self)
        self.stars.add(new_star)

    def _update_stars(self):
        """Update position of stars and get rid of old stars"""
        # Update star position
        self.stars.update()

        # Get rid of ninja stars that have disappeared.
        for star in self.stars.copy():
            if star.rect.right >= 640:
                self.stars.remove(star)

    def _update_screen(self):
         """Updates images on the screen, and flip to the new screen."""
         self.screen.fill(self.settings.bg_color)
         for star in self.stars.sprites():
             star.draw_star()
         self.ninja.blitme()
         self.skystars.draw(self.screen)

         pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance and run the game.
    the_game = Game()
    the_game.run_game()