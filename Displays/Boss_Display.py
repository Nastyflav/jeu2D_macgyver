#! /usr/bin/env python3
# coding: utf-8
import pygame as pg

from Settings.constants import *


class Boss_Display(pg.sprite.Sprite):

    def __init__(self):
        #Collaborate with the mother class
        super().__init__()
        self.image = pg.image.load(IMAGE_BOSS).convert_alpha()
        #Return the structure which allows to position sprites
        self.rect = self.image.get_rect()