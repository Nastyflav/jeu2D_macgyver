import os

from Packages.Map import *
from Packages.Position import Position
from Packages.Macgyver import MacGyver
from Packages.Boss import Boss
from Packages.Items import Items
from Packages.Map_Text_Display import Map_Text_Display
#from Settings.constants import *


class Game:

    def __init__(self):
        self.running = False
        self.map = Map('Maps/level.txt')
        self.map.load_from_file()
        
        # self.macgyver = MacGyver(map)
        # self.map.add_macgyver(macgyver)
        # self.boss = Boss(boss)
        # self.map.add_boss() 
        #self.items = Items()

    def start(self):
        self.running = True
        while self.running:
            
            # map.map_display
            # map.add_items
            # user_answer = input("Press Q to quit")
            # if user_answer == "Q":
            #     self.running = False
        
        
        #As long as self.running:
            #for each MG move:
                #print map
                #if user_answer == "Up"
                    #if  next_position is in self.map
                        #self_position = next_position
                        #print map with next_position
                    #else
                        #do nothing
                ##if user_answer == "Down"
                    #if  next_position is in self.map
                        #self_position = next_position
                        #print map with next_position
                    #else
                        #do nothing
                #if user_answer == "Right"
                    #if  next_position is in self.map
                        #self_position = next_position
                        #print map with next_position
                    #else
                        #do nothing
                #if user_answer == "Left"
                    #if  next_position is in self.map
                        #self_position = next_position
                        #print map with next_position
                    #else
                        #do nothing
        #if MG position = exit position
            #game exit
            
            
    #def direction(self):