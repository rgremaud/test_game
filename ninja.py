import pygame

from settings import Settings

class Ninja:
    """A class to manage the ninja."""

    def __init__(self, the_game):
        """Initialize the ninja and set its starting position"""
        self.screen = the_game.screen
        self.settings = the_game.settings
        self.screen_rect = the_game.screen.get_rect()

        # Load the ninja image and get its rect.
        self.image = pygame.image.load('images/ninja.bmp')
        self.rect = self.image.get_rect()

        # Start each new ninja at the center of the screen.
        self.rect.topleft = (280, 200)

        # Store a float for the ninja's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags; start w/ninja center of screen
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update ninja's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ninja_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ninja_speed
        if self.moving_up:
            self.y -= self.settings.ninja_speed
        if self.moving_down:
            self.y += self.settings.ninja_speed
        
        # Update rect object
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)