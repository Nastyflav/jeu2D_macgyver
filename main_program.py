import os

from Packages.Map import Map
from Packages.Position import Position
from Packages.Boss import Boss
from Packages.Macgyver import MacGyver
from Settings.constants import *


def main():
    map = Map('Maps/level.txt')
    macgyver = MacGyver(map)
    position = Position()
    print(macgyver.position)
    
    
    input("Choose your next move")
    
if __name__ =="__main__":
    main()







