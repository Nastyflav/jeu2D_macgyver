#! /usr/bin/env python3
# coding: utf-8
"""The hero class, managing movements and actions"""

class Macgyver:
    """Class to manage the Macgyver moves and the items picking into the maze"""
    def __init__(self, map):
        """Start position and items counter"""
        self.x = 0
        self.y = 12
        self.map = map
        self.items_collected = 0

    def move_up(self, map):
        """Check if the hero can move up and if he's on an item square"""
        if map.map_array[self.y - 1][self.x] != 'W':
            map.map_array[self.y][self.x] = '.'
            self.y -= 1
            map.map_array[self.y][self.x] = 'M'
        return map

    def move_down(self, map):
        """Check if the hero can move down and if he's on an item square"""
        if map.map_array[self.y + 1][self.x] != 'W':
            map.map_array[self.y][self.x] = '.'
            self.y += 1
            map.map_array[self.y][self.x] = 'M'
        return map

    def move_right(self, map):
        """Check if the hero can move right and if he's on an item square"""
        if map.map_array[self.y][self.x + 1] != 'W':
            map.map_array[self.y][self.x] = '.'
            self.x += 1
            map.map_array[self.y][self.x] = 'M'
        return map

    def move_left(self, map):
        """Check if the hero can move left and if he's on an item square"""
        if map.map_array[self.y][self.x - 1] != 'W':
            map.map_array[self.y][self.x] = '.'
            self.x -= 1
            map.map_array[self.y][self.x] = 'M'
        return map

    def collect_items(self, pos_y, pos_x):
        """Method to compare Macgyver position with the items positions,
        to increment the number of collected items"""
        if self.map.map_array[self.y][self.x] == 'N'\
        or 'T'\
        or 'E':
            self.items_collected += 1
