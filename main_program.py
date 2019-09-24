import os

# from Packages.Game import Game
# from Packages.Map_Text_Display import Map_Text_Display
from Packages.Map import Map
from Packages.Macgyver import Macgyver
# from Packages.Boss import Boss
from Packages.Position import Position

def main():
    map = Map("Maps/level.txt")
    macgyver = Macgyver(Map)
    print(macgyver.position)

if __name__ =="__main__":
    main()







