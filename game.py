import pygame
pygame.init()

from GameObject import GameObject, Strawberry
from GameObject import Apple
from GameObject import Strawberry
from GameObject import Player

screen_height = 500
screen_width = 500
screen = pygame.display.set_mode([screen_width, screen_height])
background_color = (0, 0, 0)

running = True

frames_per_second = 30
clock = pygame.time.Clock()

player = Player()
apple = Apple()
strawberry = Strawberry()

while running:
    # Check for a QUIT event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
    # Set the background of the screen
    screen.fill(background_color)
    
    apple.move()
    strawberry.move()

    apple.render(screen)
    strawberry.render(screen)
    player.render(screen)

    pygame.display.flip()
    clock.tick(frames_per_second * 2)
