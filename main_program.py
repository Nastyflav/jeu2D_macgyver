import os

from Packages.Map import Map
from Packages.Position import Position
from Packages.Boss import Boss
from Packages.Macgyver import MacGyver
from Packages.Items import Items
from Settings.constants import *


def main():
    map = Map('Maps/level.txt')

    items = Items(map)
    print(items.position)

    
if __name__ =="__main__":
    main()







