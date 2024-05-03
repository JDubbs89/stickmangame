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
    K_w,
    K_a,
    K_s,
    K_d,
    QUIT
)

def __init__(inWIDTH,inHEIGHT,inscreen):
    global WIDTH,HEIGHT,SCREEN
    WIDTH = inWIDTH
    HEIGHT = inHEIGHT
    SCREEN = inscreen

class Stickman(pygame.sprite.Sprite):
    def __init__(self,id):
        super(Stickman,self).__init__()
        self.id = id
        self.lives = 3
        self.surf = pygame.image.load("p1standstill.gif").convert()
        self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.surf.get_rect(center=(
                random.randint(WIDTH + 20, WIDTH + 100),
                random.randint(0, HEIGHT),
            ))
    
    def update(self, pressed_keys):
        
        if self.id == 0 and self.lives > 0:
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -5)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, 5)
            if pressed_keys[K_a]:
                self.rect.move_ip(-5, 0)
            if pressed_keys[K_d]:
                self.rect.move_ip(5, 0)
        elif self.lives > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
    
    def kill(self):
        self.lives -= 1
        if self.lives <= 0:
            self.surf.set_alpha(0)
