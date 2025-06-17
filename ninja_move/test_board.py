import pygame 

pygame.init()

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((173, 216, 230))
pygame.display.update()

pygame.display.flip()


