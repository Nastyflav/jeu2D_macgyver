import os

# from Packages.Game import Game
from Displays.Map_Text_Display import Map_Text_Display
from Models.Map import Map
from Models.Macgyver import Macgyver
from Models.Boss import Boss
from Models.Position import Position
# from Packages.Items import *

def main():
    map = Map("Maps/level.txt")
    mg = Macgyver(map)
    display = Map_Text_Display()
    display.display_map(map)
    mg.moves("right")
    display.display_map(map)
   
    

if __name__ =="__main__":
    main()







