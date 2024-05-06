import pygame, random, os

vec = pygame.math.Vector2


def __init__(inWIDTH, inHEIGHT, inscreen,game):
    global WIDTH, HEIGHT, SCREEN,GAME
    WIDTH = inWIDTH
    HEIGHT = inHEIGHT
    SCREEN = inscreen
    GAME = game

class Stickman(pygame.sprite.Sprite):
    def __init__(self, id, x, y,keys, gravity=2, friction=0.12):
        super(Stickman, self).__init__()
        self.id = id
        self.lives = 3
        self.keys = keys
        img = pygame.image.load("assets/p1standstill.gif")
        self.image = pygame.transform.scale(img, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self,keys):
        dx = 0
        dy = 0
        self.keys = keys
		#get keypresses
        if keys[pygame.K_UP] and self.jumped == False and self.id == 0:
            self.vel_y = -15
            self.jumped = True
        if keys[pygame.K_UP] == False and self.id == 0:
            jumped = False
        if keys[pygame.K_LEFT]:
            dx -= 5
        if keys[pygame.K_RIGHT]:
            dx += 5
        if keys[pygame.K_w] and self.jumped == False and self.id == 1:
            self.vel_y = -15
            self.jumped = True
        if keys[pygame.K_w] == False and self.id == 1:
            self.jumped = False
        if keys[pygame.K_a] and self.id == 1:
            dx -= 5
        if keys[pygame.K_d] and self.id == 1:
            dx += 5
        print("Hello World")
		#add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

		#check for collision

		#update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            dy = 0

		#draw player onto screen
        SCREEN.blit(self.image, self.rect)

    def kill(self):
        self.lives -= 1
        if self.lives <= 0:
            self.image.set_alpha(0)
