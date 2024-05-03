import pygame
import random

from pygame.locals import(RLEACCEL,QUIT)

def __init__(width,height,screen):
    global WIDTH,HEIGHT,SCREEN
    WIDTH = width
    HEIGHT = height
    SCREEN = screen

class Door(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Door,self).__init__()
        self.x = x
        self.y = y

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,id,sizex = 30,sizey = 10):
        super(Platform,self).__init__()
        self.x = x
        self.y = y
        self.width =  sizex
        self.height = sizey
        self.id = id
        self.surf = pygame.image.load("p1standstill.gif").convert()
        self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.surf.get_rect(center=(
                random.randint(WIDTH + 20, WIDTH + 100),
                random.randint(0, HEIGHT),
            ))

class TeamPlatform(Platform):
    def __init__(self,team):
        super(TeamPlatform,self).__init__()
        self.team = team

class AllPlatform(Platform):
    def __init__(self,team):
        super(AllPlatform,self).__init__()
        self.team = team