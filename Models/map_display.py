#! /usr/bin/env python3
# coding: utf-8
import os

from Models.map import Map


class Map_display:

    def __init__(self):
        pass

    def display_map(self, map):
        for line in map.map_array:
            for character in line:
                print(character, end=" ")
            print()