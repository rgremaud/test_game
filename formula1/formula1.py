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
        self.top_barriers = pygame.sprite.Group()
        self.bottom_barriers = pygame.sprite.Group()

        self._create_barrier()
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self._update_barrier()
            self._update_racecar()
            self.clock.tick(60)
    
    def _update_racecar(self):
        """Update the car's movement"""
        self.racecar.update()
    
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
    
    def _create_barrier(self):
        """Create a barrier"""
        barrier = Barrier(self,type='top')
        self.top_barriers.add(barrier)

        barrier = Barrier(self,type='bottom')
        self.bottom_barriers.add(barrier)
    
    def _update_barrier(self):
        self.top_barriers.update()
        self.bottom_barriers.update()

        for barrier in self.top_barriers.copy():
            if barrier.rect.left <= 0:
                self.top_barriers.remove(barrier)
                self._create_barrier()
                self.settings.increase_barrier_speed()

        for barrier in self.bottom_barriers.copy():
            if barrier.rect.left <= 0:
                self.bottom_barriers.remove(barrier)
                self._create_barrier()
        
    
    def _update_screen(self):
        """Update images on the screen and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.background.blitme()
        self.racecar.blitme()
        self.top_barriers.draw(self.screen)
        self.bottom_barriers.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance and run the game.
    race_day = Formula1()
    race_day.run_game()