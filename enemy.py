import pygame

def __init__(inscreen,inwidth,inheight):
    global SCREEN,WIDTH,HEIGHT
    SCREEN = inscreen
    WIDTH = inwidth
    HEIGHT = inheight

class Enemy(pygame.sprite.Sprite):
    def __init__(self,id,x,y):
        self.id = id
        self.posx = x
        self.posy = y
        self.hitbox = pygame.Rect(x-3, y + 4, 6, 8)
    def Combat():
        

'''
    def __init__(self):
        super(Enemy, self).__init__(PlatformX,PlatformY)
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