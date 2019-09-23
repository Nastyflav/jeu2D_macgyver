import os

from Packages.Position import Position
from Packages.Map import Map
from Settings.constants import *


class MacGyver: 

    #character initialization
    def __init__ (self, paths):
        #base map
        self.paths = map
        #character position / using property from map.py, "start" as an attribut
        self.position = map.start_square

    #character moves
    def moves (self, direction):
        #getattr access an object property using a string
        next_position = getattr(self.position, direction)()
        if next_position in self._paths:
            self.position = next_position
        return map
            #To end the game
            #if self.map._exit(position):

            
        
    #character counter
        #if MG position = item position
                #pick up item
                #implemente counter
                #MG moves
            #else
                #MG moves

