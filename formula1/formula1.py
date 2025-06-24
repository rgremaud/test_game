import sys

import pygame

from settings import Settings
from background import Background
from racecar import Racecar
from barriers import Barrier

class Formula1:
    """Formula 1 racing but as a flappy bird"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        
        pygame.display.set_caption("Formula1")

        self.background = Background(self)
        self.racecar = Racecar(self)
        self.barrier = Barrier(self)
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self._update_racecar()
            self._update_barrier()
            self.clock.tick(60)
    
    def _update_racecar(self):
        """Update the car's movement"""
        self.racecar.update()
    
    def _update_barrier(self):
        """Update the barrier's movement"""
        self.barrier.update()
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.racecar.jump()
    
    def _update_screen(self):
        """Update images on the screen and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.background.blitme()
        self.racecar.blitme()
        self.barrier.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance and run the game.
    race_day = Formula1()
    race_day.run_game()