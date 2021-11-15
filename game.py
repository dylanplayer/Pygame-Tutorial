import pygame
from pygame.locals import *
pygame.init()

from GameObject import GameObject
from GameObject import Bird1
from GameObject import Bird2
from GameObject import Bomb
from GameObject import Player

score = 0

screen_height = 500
screen_width = 500
screen = pygame.display.set_mode([screen_width, screen_height])
background_color = (0, 0, 0)

font = pygame.font.SysFont(None, 24)

all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()
bombs = pygame.sprite.Group()

running = True

frames_per_second = 30
clock = pygame.time.Clock()

bird1 = Bird1()
all_sprites.add(bird1)
fruit_sprites.add(bird1)
bird2 = Bird2()
all_sprites.add(bird2)
fruit_sprites.add(bird2)
bomb =  Bomb()
all_sprites.add(bomb)
bombs.add(bomb)
player = Player()
all_sprites.add(player)


def get_collided_sprite(player, sprite_list):
    for sprite in sprite_list:
        if pygame.Rect.colliderect(player.rect, sprite.rect):
            return sprite

frame_counter = 0

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
    
    frame_counter += 1

    if frame_counter % 5 == 0:
        bird1.update()
        bird2.update()
        player.update()
        bomb.update()

    bird1.move()
    bird2.move()
    
    collided_fruit = get_collided_sprite(player, fruit_sprites)
    if collided_fruit:
        score += 1
        collided_fruit.speed += .01
        bomb.reset()
        while (get_collided_sprite(player, bombs)) :
            bomb.reset()
        collided_fruit.reset()

    collided_bomb = get_collided_sprite(player, bombs)
    if collided_bomb:
        running = False

    for sprite in all_sprites:
        sprite.render(screen)

    score_obj = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_obj, (50,50))

    pygame.display.flip()
    clock.tick(frames_per_second * 2)
