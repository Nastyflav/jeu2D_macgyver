#! /usr/bin/env python3
# coding: utf-8
import os

from random import sample

from Settings.constants import *

class Map:

    #Map creation
    def __init__(self, filename):
        self.filename = filename
        #Lists of the entire map and of the available squares to place items
        self.map_array = []
        self.items = []
        self.items_squares = []
        # Method to create items positions
        self.load_from_file()
        self.empty_path()
        # self.random_items()
        #Pick a position in a list for each item
        # self.needle_square = self.items[0]
        # self.tube_square = self.items[1]
        # self.ether_square = self.items[2]

        self.height = None
        self.width = None
  
    #Loading map
    def load_from_file(self):
        #Load the file (filename) content into the paths attribut. Identify as well the start and exit positions
        with open(self.filename) as level:
            positions = []
            #Use enumerate in a loop to list every square and its nature
            for x, line in enumerate(level):
                line_display = []
                for y, col in enumerate(line):
                    line_display.append(col)
                    #if there is a path square ('.' as PATH_CHAR)
                    if col == PATHS_SQUARE:
                        self.map_array.append(line_display)
                        positions.append((x, y)
                return positions
                self.map_array.append(line_display)                    
            #Calculating square dimensions
            self.height = x + 1
            self.width = y + 1

            def empty_path(self, labyrinth_map):
    positions = []
    for y, line in enumerate(labyrinth_map):
        for x, column in enumerate(line):
            if column == " ":
                positions.append((x,y))
    return positions
self._path = self.empty_path(self._labyrinth)
    
    # def random_items(self):
    #     #Position three items into the maze, using random.sample to pick
    #     self.items = sample(self.items_squares, 3)
