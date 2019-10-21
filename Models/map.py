#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg
from random import sample

from Settings.constants import PATHS_SQUARE

class Map:

    #Map creation
    def __init__(self, filename):
        self.filename = filename
        #Lists of the entire map and of the available squares to place items
        self.map_array = []
        self.items = []
        # Method to create items positions
        self.load_from_file()
        self.random_items(self.map_array)

        self.height = None
        self.width = None
  
    #Loading map to make an array with all the file characters
    def load_from_file(self):
        try:
            with open(self.filename, "r") as map_file:
                for line in map_file:
                    self.map_array.append(list(line.strip()))
        except FileNotFoundError:
            print("Couldn't open map file \"" + self.filename + "\"")
            exit() 
 
    #Method to extract every path position into the map_array, and using the random.sample function to select three items positions
    def random_items(self, map_array):
        positions = []
        for x, line in enumerate(self.map_array):
            for y, column in enumerate(line):
                if column == PATHS_SQUARE:
                    positions.append((x,y))
        self.items = sample(positions, 3)
        #We place every item into the maze, using a character for every one of them
        self.map_array[self.items[0][0]][self.items[0][1]] = 'N'
        self.map_array[self.items[1][0]][self.items[1][1]] = 'T'
        self.map_array[self.items[2][0]][self.items[2][1]] = 'E'

