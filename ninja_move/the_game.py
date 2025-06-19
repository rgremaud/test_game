import sys

import pygame

from settings import Settings
from ninja import Ninja
from ninja_star import Star
from sky_star import Skystar
from badguy import Badguy
from random import randint
from game_stats import GameStats
from button import Button

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
        self.badguys = pygame.sprite.Group()

        self.stats = GameStats(self)

        self._create_sky()
        self._create_badguys()
        self.game_active = False

        # Make the play button.
        self.play_button = Button(self, "Play")
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ninja.update()
                self._update_stars()
                self._update_badguys()

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game statistics
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining ninja stars
            self.stars.empty()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

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
    
    def _check_badguy_edges(self):
        """Respond appropriately when badguy hit edge"""
        for badguy in self.badguys.sprites():
            if badguy.check_edges():
                self._change_badguy_direction()
                break
    
    def _change_badguy_direction(self):
        """Change the badguy's direction"""
        for badguy in self.badguys.sprites():
            self.settings.badguy_direction *= -1

    def _create_sky(self):
        """Create a night sky."""
        # Create a star and keep adding until no room is left.
        # Spacing between star is two star width
        skystar = Skystar(self)
        skystar_width, skystar_height = skystar.rect.size

        current_x, current_y= skystar_width * 2, skystar_height * 2
        while current_y < (self.settings.screen_height - 20 * skystar_height):
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

    def _create_badguys(self):
        """Create badguys"""
        # Make a badguy
        badguy = Badguy(self)
        self.badguys.add(badguy)

    def _fire_star(self):
        """Create a new star and add it to the star group."""
        new_star = Star(self)
        self.stars.add(new_star)

    def _update_stars(self):
        """Update position of stars and get rid of old stars"""
        # Update star position
        self.stars.update()
        self._update_badguys()
        # Get rid of ninja stars that have disappeared.
        for star in self.stars.copy():
            if star.rect.right >= 640:
                self.stars.remove(star)
        
        # Check if any ninjastars have hit the bad guy
        self._ninja_hit()
    
    def _ninja_hit(self):
        """Check if red ninja has been hit"""
        if self.stats.badguy_life_left > 0:
            if pygame.sprite.groupcollide(self.stars, self.badguys, True, False):
                self.stats.badguy_life_left -= 1
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            print("Congratulations.  You defeated the red ninja!")
    
    def _update_badguys(self):
        """Update the position of the badguy"""
        self.badguys.update()
        self._check_badguy_edges()

    def _update_screen(self):
         """Updates images on the screen, and flip to the new screen."""
         self.screen.fill(self.settings.bg_color)
         for star in self.stars.sprites():
             star.draw_star()
         self.ninja.blitme()
         self.badguys.draw(self.screen)
         self.skystars.draw(self.screen)

         # Draw play button if the game is inactive.
         if not self.game_active:
             self.play_button.draw_button()

         pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance and run the game.
    the_game = Game()
    the_game.run_game()