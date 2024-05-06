import pygame, random, os

vec = pygame.math.Vector2
from pygame.locals import (
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
    QUIT,
)


def __init__(inWIDTH, inHEIGHT, inscreen):
    global WIDTH, HEIGHT, SCREEN
    WIDTH = inWIDTH
    HEIGHT = inHEIGHT
    SCREEN = inscreen


class Stickman(pygame.sprite.Sprite):
    def __init__(self, id, posx, posy, gravity=2, friction=0.12):
        super(Stickman, self).__init__()
        self.id = id
        self.lives = 3
        self.grav = gravity
        self.fric = friction
        self.surf = pygame.image.load("assets/p1standstill.gif").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            midbottom=(
                posx,
                posy,
            )
        )
        self.pos = vec(posx, posy)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:

                if self.id == 0 and self.lives > 0:
                    self.vel = vec(0, 0.5)
                    if event.key == K_a:
                        self.acc.x = -0.5
                    if event.key == K_d:
                        self.acc.x = 0.5
                elif self.lives > 0:
                    if event.key == K_LEFT:
                        self.acc.x = -0.5
                    if event.key == K_RIGHT:
                        self.acc.x = 0.5

        self.acc.x += self.vel.x * self.fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

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
