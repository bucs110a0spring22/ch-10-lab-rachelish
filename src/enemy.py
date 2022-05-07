import pygame
import random
from src import controller
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2
        

    def update(self):  
      '''randomizes enemy motion + keeps them in screen'''
      self.rect.x += random.randint(-1, 1)
      self.rect.y += random.randint(-1, 1)

      if self.rect.x <= 0 or self.rect.x >=400 or self.rect.y <= 0 or self.rect.y >= 400:
        self.rect.x = 200
        self.rect.y = 200



      

      

        
      
