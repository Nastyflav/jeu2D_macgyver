import os


class Items:

    n = "N"
    p = "P"
    e = "E"
    
    #items initialization
    def _init__(self, n, p, e, map):
        #base map
        self.map = map
        self.n_position = self.needle
        self.p_position = self.plastic_tube
        self.e_position = self.ether
