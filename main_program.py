#! /usr/bin/env python3
# coding: utf-8
import os

# from Models.Game import Game
# from Models.map_display import Map_Display
from Models.map import Map
from Models.macgyver import Macgyver
from Models.game import Game
# from Models.Items import *

def main():
    # map = Map("Maps/level.txt")
    # display = Map_Display()
    # display.display_map(map)
    # mg = Macgyver()
    # map = mg.move_up(map)
    # display.display_map(map)
    # map = mg.move_down(map)
    # display.display_map(map)

    game = Game()
    game.start()
   
    

if __name__ =="__main__":
    main()







