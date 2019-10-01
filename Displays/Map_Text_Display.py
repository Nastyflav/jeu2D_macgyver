#! /usr/bin/env python3
# coding: utf-8
import os

from Models.Map import Map
from Models.Position import Position

#A class to play with the terminal mode
class Map_Text_Display():
    def __init__(self):
        pass

    #Display map stored in Map class
    def display_map(self, map):    
        for x, line_number in range(0, 14) in map.map_array:
            for y, col_number in range (0, 14) in line_number:
                position = Position(x, y)
                if position == map.start_square:
                        print('S')
                elif position == map.exit_square:
                        print('E')
                elif position == map.needle_square:
                        print('N')
                elif position == map.tube_square:
                        print('T')
                elif position == map.ether_square:
                        print('X')
                elif position == map._paths:
                        print('.')
                else:
                        print("#")

    # def display_map(self, map):
    #     for line in map._paths:
    #         for character in line:
    #             print(character, end="")
    #     print()