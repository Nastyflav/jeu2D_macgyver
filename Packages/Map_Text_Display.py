import os

from Packages.Map import Map


class Map_Text_Display():
    def __init__(self):
        pass
    ##
    ## Display map stored in Map class
    ##
    def display_map(self, map):
        for line in map.map_array:
            for character in line:
                print(character, end="")
            print()