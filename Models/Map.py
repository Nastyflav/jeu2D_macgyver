import os
from random import sample

from Packages.Position import Position
from Packages.Macgyver import Macgyver
from Packages.Items import Needle
from Settings.constants import *


class Map:

    #Map creation
    def __init__(self, filename):
        self.filename = filename
        
        #Lists of the entire map and of the available squares to place items
        self.map_array = []
        self.items = []
        # Some sets to store the different kind of positions
        self._start = set()
        self._exit = set() 
        self._paths = set()
        self.items_squares = set()
        #Methods to lauch to determinate positions
        self.load_from_file()
        self.random_items()
        #Pick a position for each item
        self.needle_square = self.items[0]
        self.tube_square = self.items[1]
        self.ether_square = self.items[2]

        self.macgyver = None
        self.boss = None
        self.height = None
        self.width = None
  
    #Loading map
    def load_from_file(self):
        #Load the file (filename) content into the paths attribut. Identify as well the start and exit positions
        with open(self.filename) as level:
            #Use enumerate in a loop to list every square and its nature
            for x, line in enumerate(level):
                line_display = []
                for y, col in enumerate(line):
                    line_display.append(col)
                    #if there is a path square ('.' as PATH_CHAR)
                    if col == PATHS_SQUARE:
                        self._paths.add(Position(x, y))
                        self.items_squares.add(Position(x, y))
                    #if this is the start square('S' as START_CHAR)   
                    elif col == START_SQUARE:
                        self._start.add(Position(x, y))
                        self._paths.add(Position(x, y))
                    #if this is the exit square ('E' as EXIT_CHAR)       
                    elif col == EXIT_SQUARE:
                        self._exit.add(Position(x, y))
                        self._paths.add(Position(x, y)) 
                self.map_array.append(line_display)                    
            #Calculating square dimensions
            self.height = x + 1
            self.width = y + 1

#I want to relate the exit position to its own value, not an action
    @property
    def exit_square(self):
        return list(self._exit)[0]

    #I want to relate the start position to its own value, not an action
    @property
    def start_square(self):
        return list(self._start)[0]

    #is a position an available path ?
    def add_paths(self, position):
        return position in self._paths 

    def add_macgyver (self, macgyver):
        #Position MacGyver into the maze
        self.macgyver = macgyver
        #MacGyver start position
        self.macgyver.position = self._start
        #So that MG can communicate with the Map class ?
        self.macgyver.Map = self

    def add_boss (self, boss):
        #Position the boss in the labyrinth
        self.boss = boss
        #Boss start position
        self.boss.position = self._exit
        #So that the boss can communicate with the Map class ?
        self.boss.Map = self

    def random_items(self):
        #Position three items into the maze, using random.sample to pick
        self.items = sample(self.items_squares, 3)
        
    def add_items(self, needle, tube, ether):
        self.needle = needle
        self.needle.position = self.needle_square
        self.needle.Map = self
        self.tube = tube
        self.tube.position = self.tube_square
        self.tube.Map = self
        self.ether = ether
        self.ether.position = self.ether_square
        self.ether.Map = self




      

    
