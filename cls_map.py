from constants import
#import pygame
#from pygame.locals import * 
#from constants import *

class Map:

    #Map creation
    def __init__(self, filename):
        self.filename = filename
        #Start
        self.start = set()
        #Exit
        self.exit = set() 
        #Paths
        self.paths = set()

        self.load_from_file()

    def available_path(self, position):
        return position in self.paths

    #Loading map
    def load_from_file(self):

        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, c in enumerate(line):
                    if c == constants.PATHS_CHAR:
                        self.paths.add(Position, (x, y))
                    elif c == constants.START_CHAR:
                        self.start.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif c == constants.EXIT_CHAR:
                        self.exit.add(Position(x, y))
                        self.paths.add(Position(x, y))






