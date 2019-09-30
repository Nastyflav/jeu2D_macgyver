import pygame as pg

from Settings.constants import *


class Needle_Display(pg.sprite.Sprite):

    def __init__(self):
        #Collaborate with the mother class
        super().__init__()
        self.image = pg.image.load(IMAGE_NEEDLE).convert_alpha()
        #Return the structure which allows to position sprites
        self.rect = self.image.get_rect()

class Tube_Display(pg.sprite.Sprite):

    def __init__(self):
        #Collaborate with the mother class
        super().__init__()
        self.image = pg.image.load(IMAGE_TUBE).convert_alpha()
        #Return the structure which allows to position sprites
        self.rect = self.image.get_rect()

class Ether_Display(pg.sprite.Sprite):

    def __init__(self):
        #Collaborate with the mother class
        super().__init__()
        self.image = pg.image.load(IMAGE_ETHER).convert_alpha()
        #Return the structure which allows to position sprites
        self.rect = self.image.get_rect()