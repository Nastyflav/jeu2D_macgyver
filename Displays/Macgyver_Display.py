#! /usr/bin/env python3
# coding: utf-8
import pygame as pg

from Settings.constants import *


class Macgyver_Display(pg.sprite.Sprite):

    def __init__(self):
        #Collaborate with the mother class
        super().__init__()
        self.image = pg.image.load(IMAGE_MACGYVER).convert_alpha()
        #Return the structure which allows to position sprites 
        self.rect = self.image.get_rect()

    def next_position(self):
        #Method which updates every MG next position
