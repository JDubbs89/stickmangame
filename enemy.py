import pygame
import random
from pygame.locals import (
    RLEACCEL)
def __init__(inscreen,inwidth,inheight):
    global SCREEN,WIDTH,HEIGHT
    SCREEN = inscreen
    WIDTH = inwidth
    HEIGHT = inheight

class Enemy(pygame.sprite.Sprite):
    def __init__(self,id,x,y,):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.id = id
        self.posx = x
        self.posy = y
        self.rect = self.surf.get_rect(
            center=(
                random.randint(WIDTH + 20, WIDTH + 100),
                random.randint(0, HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
   # def Update():
        

'''
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("").convert()
        # The starting position is based on the platforms position
        self.rect = self.surf.get_rect(
            center=(PlatformX, PlatformY + 1)
        )
        self.speed = #MOVESPEED


    def update(self):
        #MOVEMENT
        #Death Parameter
            self.kill()'''