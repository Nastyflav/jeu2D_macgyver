#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg

from Settings.constants import *


class Macgyver:
    def __init__(self):
        #Character start position
        self.x = 0
        self.y = 12

    # Four different movements for the character
    def move_up(self, map):
        if map.map_array[self.y - 1][self.x] != 'W':
            map.map_array[self.y][self.x] = '.'
            self.y -= 1
            map.map_array[self.y][self.x] = 'M'
        return map

    def move_down(self, map):
        if map.map_array[self.y + 1][self.x] != 'W':
            map.map_array[self.y][self.x] = '.'
            self.y += 1
            map.map_array[self.y][self.x] = 'M'
        return map

    def move_right(self, map):
        if map.map_array[self.y][self.x + 1] != 'W':
            map.map_array[self.y][self.x] = '.'
            self.x += 1
            map.map_array[self.y][self.x] = 'M'
        return map

    def move_left(self, map):
        if map.map_array[self.y][self.x - 1] != 'W':
            map.map_array[self.y][self.x] = '.'
            self.x -= 1
            map.map_array[self.y][self.x] = 'M'
        return map

    def pick_up_object(self):
        pass


class Macgyver_display(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.image.load(IMAGE_MACGYVER).convert_alpha()
        self.rect = self.image.get_rect()

    