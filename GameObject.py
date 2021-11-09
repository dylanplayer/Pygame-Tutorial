import pygame
import random

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'apple.png')
    self.dx = 0
    self.dy = (random.randint(0, 200) / 100) + 1
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
    # Check the y position of the apple
    if self.y > 500: 
      self.reset()

  # add a new method
  def reset(self):
    self.x = random.randint(50, 400)
    self.y = -64

class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'strawberry.png')
    self.dx = (random.randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
    # Check the y position of the apple
    if self.x > 500: 
      self.reset()

  # add a new method
  def reset(self):
    self.x = -64
    self.y = random.randint(50, 400)

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0,0, 'player.png')
        self.dx = 10
        self.dy = 10
        self.reset()

    def left(self):
        self.x -= self.dx
    
    def right(self):
        self.x += self.dx

    def up(self):
        self.y -= self.dy

    def down(self):
        self.y += self.dy

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32