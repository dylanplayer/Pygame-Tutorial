import pygame
import random

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
    self.speed = 1

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'apple.png')
    self.dx = 0
    self.dy = (random.randint(0, 200) / 100) + 1
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > 500: 
      self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def reset(self):
    self.dy = ((random.randint(0, 200) / 100) + 1) * self.speed
    self.x = random.randint(50, 400)
    self.y = -64

class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0, 0, 'bomb.png')
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def reset(self):
    self.x = random.randint(50, 400)
    self.y = random.randint(50, 400)
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'strawberry.png')
    self.dx = (random.randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500: 
      self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def reset(self):
    self.dx = ((random.randint(0, 200) / 100) + 1) * self.speed
    self.x = -64
    self.y = random.randint(50, 400)

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0,0, 'player.png')
        self.dx = 30
        self.dy = 30
        self.x = 250
        self.y = 250
        self.reset()
        self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))


    def left(self):
        self.x -= self.dx
        self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))
    
    def right(self):
        self.x += self.dx
        self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

    def up(self):
        self.y -= self.dy
        self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

    def down(self):
        self.y += self.dy
        self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32