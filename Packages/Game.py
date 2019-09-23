import os

from Packages.Map import Map
from Packages.Position import Position
from Packages.Macgyver import MacGyver
from Packages.Boss import Boss
from Packages.Items import Items
#from Settings.constants import *


class Game:

    def __init__(self):
        
        self.map = Map('Maps/level.txt')
        self.map.load_from_file()
        # self.macgyver = MacGyver(map)
        # self.map.add_macgyver(macgyver)
        #self.boss = Boss(map)
        #self.map.add_boss(boss) 
        #self.items = Items()

    def start(self):
         

        # maptextdisplay = Map_Text_Display(map)
        # maptextdisplay.level()
        # user_answer = input ("Choose your move")
        # while user_answer != "Q":
        #     if user_answer == "up":
        #         map.macgyver.moves("up")
        #     maptextdisplay.level
        #     input ("Choose your move")
        
        
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