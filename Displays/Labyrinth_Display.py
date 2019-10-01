#! /usr/bin/env python3
# coding: utf-8
import pygame as pg

from Settings.constants import *


class Labyrinth_Display(pg.sprite.Sprite):

    def __init__(self):
        #Collaborate with the mother class
        super().__init__()
        self.image = pg.image.load(IMAGE_BACKGROUND).convert()
        #Return the structure which allows to position sprites
        self.rect = self.image.get_rect()

    def funcname(self, parameter_list):
    #For each labyrinth position, print an image that matched 

