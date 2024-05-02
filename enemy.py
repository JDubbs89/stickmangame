import pygame

class Enemy():
    def __init__(self,id,x,y):
        self.id = id
        self.posx = x
        self.posy = y
        self.hitbox = Rect(posx-3, posy + 4, 6, 8)
    