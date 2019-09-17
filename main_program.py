import os

from Packages.Map import Map
from Packages.Position import Position
from Packages.Boss import Boss
from Packages.Macgyver import MacGyver
from Settings.constants import *


def main():
    map = Map('Maps/level.txt')
    p = Position(12, 1)
    print(map.available_paths(p))

    
if __name__ =="__main__":
    main()







