import pygame

class Rainman:
    """A class to manage the rainman"""

    def __init__(self, rainmaker):
        """Initialize a rainman and set the starting position"""
        self.screen = rainmaker.screen
        self.settings = rainmaker.settings
        self.screen_rect = rainmaker.screen.get_rect()

        # Load the rainman image and get its rect.
        self.image = pygame.image.load('images/rainman.bmp')
        self.rect = self.image.get_rect()

        # Start each ninja at bottom middle of screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the rainman's exact position
        self.x = float(self.rect.x)

        # Movement flags; allow movement on x-axis
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update rainman's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rainman_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rainman_speed

        # Update rect object
        self.rect.x = self.x
    
    def blitme(self):
        """Draw rainman at his current location"""
        self.screen.blit(self.image, self.rect)