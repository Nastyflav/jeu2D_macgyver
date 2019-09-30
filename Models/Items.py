import os

from Models.Position import Position


class Needle:    
    #character initialization
    def __init__ (self, map):
        #base map
        self.map = map
        #Its position is stored in Map
        self.position = self.map.needle_square

class Tube:    
    #character initialization
    def __init__ (self, map):
        #base map
        self.map = map
        #Its position is stored in Map
        self.position = self.map.tube_square

class Ether:    
    #character initialization
    def __init__ (self, map):
        #base map
        self.map = map
        #Its position is stored in Map
        self.position = self.map.ether_square