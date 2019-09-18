import os
from random import sample

from Packages.Position import Position
from Packages.Macgyver import MacGyver
from Packages.Boss import Boss
from Packages.Items import Items
from Settings.constants import *

class Map:

    #Map creation
    def __init__(self, filename):
        self.filename = filename
        #Start
        self._start = set()
        #Exit
        self._exit = set() 
        #Paths
        self._paths = set()
        #Macgyver
        self.macgyver = None
        #Boss
        self.boss = None
        #Items
        self.items = None
        #Maze dimensions
        self.height = None
        self.width = None
        #File attribut
        self.load_from_file()

    #I want to relate the start position to its own value, not an action
    @property
    def start(self):
        return list(self._start)[0]

    #I want to relate the exit position to its own value, not an action
    @property
    def exit(self):
        return list(self._exit)[0]

    #is a position an available path ?
    def available_paths(self, position):
        return position in self._paths

    #Loading map
    def load_from_file(self):
        #Load the file (filename) content into the paths attribut. Identify as well the start and exit positions
        with open(self.filename) as infile:
            #Use enumerate in a loop to list every square and its nature
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    #if there is a path square ('.' as PATH_CHAR)
                    if col == PATHS_SQUARE:
                        self._paths.add(Position(x, y))
                    #if this is the start square('S' as START_CHAR)   
                    elif col == START_SQUARE:
                        self._start.add(Position(x, y))
                        self._paths.add(Position(x, y))
                    #if this is the exit square ('E' as EXIT_CHAR)       
                    elif col == EXIT_SQUARE:
                        self._exit.add(Position(x, y))
                        self._paths.add(Position(x, y))
                        
            #Calculating square dimensions
            self.height = x + 1
            self.width = y + 1
        
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

    def add_items(self, n, p_t, e):
        #Position the items into the maze, using random.sample to pick each one
        n = random.sample(set([self._paths]), 1)
        p_t = random.sample(set([self._paths]), 1)
        e = random.sample(set([self._paths]), 1)
      
        
