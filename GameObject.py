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

class Bird2(GameObject):
  def __init__(self):
    self.imgIndex = 0
    self.images = ['bird/bird1.png','bird/bird2.png','bird/bird3.png','bird/bird4.png','bird/bird5.png','bird/bird6.png','bird/bird7.png','bird/bird8.png',]
    super(Bird2, self).__init__(0, 0, self.images[self.imgIndex])
    self.dx = 0
    self.dy = (random.randint(0, 200) / 100) + 1
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def update(self):
      if self.imgIndex < len(self.images)-1:
        self.imgIndex += 1
      else:
        self.imgIndex = 0
      self.surf = pygame.image.load(self.images[self.imgIndex])

  def move(self):
    self.x += self.dx
    self.y -= self.dy
    if self.y < 0: 
      self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def reset(self):
    self.dy = ((random.randint(0, 200) / 100) + 1) * self.speed
    self.x = random.randint(50, 400)
    self.y = 550

class Bomb(GameObject):
  def __init__(self):
    self.imgIndex = 0
    self.images = ['bomb/bomb1.gif','bomb/bomb2.gif','bomb/bomb3.gif','bomb/bomb4.gif']
    super(Bomb, self).__init__(0, 0, self.images[self.imgIndex])
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def update(self):
    if self.imgIndex < len(self.images)-1:
      self.imgIndex += 1
    else:
      self.imgIndex = 0
    self.surf = pygame.image.load(self.images[self.imgIndex])

  def reset(self):
    self.x = random.randint(50, 400)
    self.y = random.randint(50, 400)
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

class Bird1(GameObject):
  def __init__(self):
    self.imgIndex = 0
    self.images = ['bird/bird1.png','bird/bird2.png','bird/bird3.png','bird/bird4.png','bird/bird5.png','bird/bird6.png','bird/bird7.png','bird/bird8.png',]
    super(Bird1, self).__init__(0, 0, self.images[self.imgIndex])
    self.dx = (random.randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def update(self):
    if self.imgIndex < len(self.images)-1:
      self.imgIndex += 1
    else:
      self.imgIndex = 0
    self.surf = pygame.image.load(self.images[self.imgIndex])

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
      self.imgIndex = 0
      self.images = ['catcher/catcher1.gif','catcher/catcher2.gif','catcher/catcher3.gif','catcher/catcher4.gif','catcher/catcher5.gif','catcher/catcher6.gif','catcher/catcher7.gif','catcher/catcher8.gif',]
      super(Player, self).__init__(0,0, self.images[self.imgIndex])
      self.dx = 30
      self.dy = 30
      self.x = 250
      self.y = 250
      self.reset()
      self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

    def update(self):
      if self.imgIndex < len(self.images)-1:
        self.imgIndex += 1
      else:
        self.imgIndex = 0
      self.surf = pygame.image.load(self.images[self.imgIndex])

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