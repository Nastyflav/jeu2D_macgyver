import os

from Packages.Map import Map
from Packages.Position import Position
from Settings.constants import *


class Boss:

    #character initialization
    def __init__ (self, map):
        #base map
        self.map = map
        #character position / using property from map.py, exit as an attribut
        self.position = self.map.exit_square

        
    

