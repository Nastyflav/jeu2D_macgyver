#! /usr/bin/env python3
# coding: utf-8
"""We only import the function sample from random module"""
from random import sample

from Settings.constants import PATHS_SQUARE, START_SQUARE


class Map:
    """Class which reads the map file, extract all the characters and places items randomly"""

    def __init__(self, filename):
        """Lists of the entire map and of all the available squares to place items"""
        self.filename = filename
        self.map_array = []
        self.items = []
        self.start_x = []
        self.start_y = []
        """Method to create positions"""
        self.load_from_file()
        self.random_items()

    def load_from_file(self):
        """Loading map to make an array with all the file characters"""
        try:
            with open(self.filename, "r") as map_file:
                for line in map_file:
                    self.map_array.append(list(line.strip()))
        except FileNotFoundError:
            print("Couldn't open map file \"" + self.filename + "\"")

    def random_items(self):
        """Method to extract every path position into the map_array
        and using the random.sample function to select three items positions"""
        positions = []
        start = []
        for x, line in enumerate(self.map_array):
            for y, column in enumerate(line):
                if column == PATHS_SQUARE:
                    positions.append((x, y))
                elif column == START_SQUARE:
                    start.append((x, y))
        self.items = sample(positions, 3)
        self.map_array[self.items[0][0]][self.items[0][1]] = 'N'
        self.map_array[self.items[1][0]][self.items[1][1]] = 'T'
        self.map_array[self.items[2][0]][self.items[2][1]] = 'E'
        self.start_x = start[0][0]
        self.start_y = start[0][1]
