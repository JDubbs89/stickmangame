import pygame, random, character, enemy, menu


from pygame.locals import RLEACCEL, QUIT


def __init__(width, height, screen):
    global WIDTH, HEIGHT, SCREEN
    WIDTH = width
    HEIGHT = height
    SCREEN = screen


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Door, self).__init__()
        self.x = x
        self.y = y
        self.surf = pygame.image.load("30x10greyplatform.gif").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(WIDTH + 20, WIDTH + 100),
                random.randint(0, HEIGHT),
            )
        )


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, id, sizex=30, sizey=10):
        super(Platform, self).__init__()
        self.x = x
        self.y = y
        self.width = sizex
        self.height = sizey
        self.id = id
        self.surf = pygame.image.load("assets/30x10greyplatform.gif").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(WIDTH + 20, WIDTH + 100),
                random.randint(0, HEIGHT),
            )
        )

    def land(self, player):
        pass


class TeamPlatform(Platform):
    def __init__(self, team):
        super(TeamPlatform, self).__init__()
        self.team = team

    def land(self, player):
        super(TeamPlatform, self).land()
        if player.team != self.team:
            player.kill()
