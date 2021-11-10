import pygame
from pygame.locals import *
pygame.init()

from GameObject import GameObject
from GameObject import Apple
from GameObject import Strawberry
from GameObject import Bomb
from GameObject import Player

points = 0

screen_height = 500
screen_width = 500
screen = pygame.display.set_mode([screen_width, screen_height])
background_color = (0, 0, 0)

all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()
bombs = pygame.sprite.Group()

running = True

frames_per_second = 30
clock = pygame.time.Clock()

apple = Apple()
all_sprites.add(apple)
fruit_sprites.add(apple)
strawberry = Strawberry()
all_sprites.add(strawberry)
fruit_sprites.add(strawberry)
bomb =  Bomb()
all_sprites.add(bomb)
bombs.add(bomb)
player = Player()
all_sprites.add(player)

def get_collided_sprite(player, sprite_list):
    for sprite in sprite_list:
        if pygame.Rect.colliderect(player.rect, sprite.rect):
            return sprite

while running:
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
    screen.fill(background_color)
    
    apple.move()
    strawberry.move()
    
    collided_fruit = get_collided_sprite(player, fruit_sprites)
    if collided_fruit:
        points += 1
        collided_fruit.speed += .2
        bomb.reset()
        while (get_collided_sprite(player, bombs)) :
            bomb.reset()
        collided_fruit.reset()

    collided_bomb = get_collided_sprite(player, bombs)
    if collided_bomb:
        running = False

    for sprite in all_sprites:
        sprite.render(screen)

    pygame.display.flip()
    clock.tick(frames_per_second * 2)
