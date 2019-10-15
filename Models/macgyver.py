#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg

from Settings.constants import *


class Macgyver:
    def __init__(self, map):
        #Character start position and image
        self.x = 0
        self.y = 12
        self.map = map
        self.items_collected = 0

    #Four different movements for the character
    def move_up(self, map):
        if map.map_array[self.y - 1][self.x] != 'W':
            map.map_array[self.y][self.x] = '.'
            self.y -= 1
            map.map_array[self.y][self.x] = 'M'
        #Some specific lines to allows MG to pick up the items
        elif map.map_array[self.y - 1][self.x] == 'N':
            map.map_array[self.y][self.x] = '.'
            self.y -= 1
            map.map_array[self.y][self.x] = 'M'
            self.items_collected += 1
        elif map.map_array[self.y - 1][self.x] == 'T':
            map.map_array[self.y][self.x] = '.'
            self.y -= 1
            map.map_array[self.y][self.x] = 'M'
            self.items_collected += 1
        elif map.map_array[self.y - 1][self.x] == 'E':
            map.map_array[self.y][self.x] = '.'
            self.y -= 1
            map.map_array[self.y][self.x] = 'M'
            self.items_collected += 1
        return map

    def move_down(self, map):
        if self.y < (SPRITE_NUMBER - 1):
            if map.map_array[self.y + 1][self.x] != 'W':
                map.map_array[self.y][self.x] = '.'
                self.y += 1
                map.map_array[self.y][self.x] = 'M'
            #Some specific lines to allows MG to pick up the items
            elif map.map_array[self.y + 1][self.x] == 'N':
                map.map_array[self.y][self.x] = '.'
                self.y += 1
                map.map_array[self.y][self.x] = 'M'
                self.items_collected += 1
            elif map.map_array[self.y + 1][self.x] == 'T':
                map.map_array[self.y][self.x] = '.'
                self.y += 1
                map.map_array[self.y][self.x] = 'M'
                self.items_collected += 1
            elif map.map_array[self.y + 1][self.x] == 'E':
                map.map_array[self.y][self.x] = '.'
                self.y += 1
                map.map_array[self.y][self.x] = 'M'
                self.items_collected += 1
        return map

    def move_right(self, map):
        if self.x < (SPRITE_NUMBER - 1):
            if map.map_array[self.y][self.x + 1] != 'W':
                map.map_array[self.y][self.x] = '.'
                self.x += 1
                map.map_array[self.y][self.x] = 'M'
            #Some specific lines to allows MG to pick up the items
            elif map.map_array[self.y][self.x + 1] == 'N':
                map.map_array[self.y][self.x] = '.'
                self.x += 1
                map.map_array[self.y][self.x] = 'M'
                self.items_collected += 1
            elif map.map_array[self.y][self.x + 1] == 'T':
                map.map_array[self.y][self.x] = '.'
                self.x += 1
                map.map_array[self.y][self.x] = 'M'
                self.items_collected += 1
            elif map.map_array[self.y][self.x + 1] == 'E':
                map.map_array[self.y][self.x] = '.'
                self.x += 1
                map.map_array[self.y][self.x] = 'M'
                self.items_collected += 1
        return map

    def move_left(self, map):
        if self.x < (SPRITE_NUMBER):
            if map.map_array[self.y][self.x - 1] != 'W':
                map.map_array[self.y][self.x] = '.'
                self.x -= 1
                map.map_array[self.y][self.x] = 'M'
            #Some specific lines to allows MG to pick up the items
            elif map.map_array[self.y][self.x - 1] == 'N':
                map.map_array[self.y][self.x] = '.'
                self.x -= 1
                map.map_array[self.y][self.x] = 'M'
                self.items_collected += 1
            elif map.map_array[self.y][self.x - 1] == 'T':
                map.map_array[self.y][self.x] = '.'
                self.x -= 1
                map.map_array[self.y][self.x] = 'M'
                self.items_collected += 1
            elif map.map_array[self.y][self.x - 1] == 'E':
                map.map_array[self.y][self.x] = '.'
                self.x -= 1
                map.map_array[self.y][self.x] = 'M'
                self.items_collected += 1
        return map
    