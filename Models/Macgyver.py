#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg


#Class to manage the Macgyver moves and the items picking into the maze
class Macgyver:

    #Start position and items counter
    def __init__(self, map):
        self.x = 0
        self.y = 12
        self.map = map
        self.items_collected = 0

    #Four different movements for the character (up, down, right, left)
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

    #Method to compare Macgyver position with the items positions, to increment the number of collected items
    def collect_items(self, map, pos_y, pos_x):
        if self.map.map_array[self.y][self.x] == 'N'\
        or 'T'\
        or 'E':
            self.items_collected += 1