#! /usr/bin/env python3
# coding: utf-8
import os

from Models.Map import Map
from Models.Position import Position
from Models.Macgyver import Macgyver
from Models.Boss import Boss
from Models.Items import *
from Displays.Map_Text_Display import Map_Text_Display
from Settings.constants import *


class Game:

    def __init__(self):
        self.map = Map('Maps/level.txt')
        self.map.load_from_file()
        self.macgyver = Macgyver(map)
        self.map.add_macgyver(self.macgyver)
        self.boss = Boss(map)
        self.map.add_boss(self.boss) 
        self.needle = Needle(map)
        self.tube = Tube(map)
        self.ether = Ether(map)
        self.map.add_items(self.needle, self.tube, self.ether)

        self.keyboard = Keyboard()

        self.running = False
        self.clock = pg.time.Clock()

    def start(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            
            # user_answer = input("Press Q to quit")
            # display.display_map(map)
            # # map.add_items
            # if user_answer == "up"
            #     mg.moves("up")
            #     display.display_map(map)
            # if user_answer == "down"
            #     mg.moves("down")
            #     display.display_map(map)
            # if user_answer == "right"
            #     mg.moves("right")
            #     display.display_map(map)
            # if user_answer == "left"
            #     mg.moves("left")
            #     display.display_map(map)
            # if user_answer == "Q":
                self.running = False
        
         
            
    #def direction(self):