import os

from Packages.Position import Position
from Settings.constants import *

class Items:

    n = "N"
    p_t = "P"
    e = "E"
    
    #items initialization
    def _init__(self, map):
        #base map
        self.map = map
        self.position = self.map.items
