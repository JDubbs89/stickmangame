import pygame
import random
from pygame.locals import(
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    K_SPACE,
    K_d,
    K_u,
    K_l,
    K_r,
    QUIT
)

class Stickman(pygame.sprite.Sprite):
    def __init__(self,id):
        super(Stickman,self).__init__()
        self.id = id
        self.surf = pygame.image.load("player.gif").convert()
        self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.surf.get_rect()