import os

from Packages.Map import Map
from Packages.Position import Position
from Packages.Macgyver import MacGyver
from Packages.Boss import Boss
from Packages.Items import Items
from Settings.constants import *


class Game:

    def __init__(self):
        
        self.map = Map('Maps/level.txt')
        self.map.load_from_file()
        #self.macgyver = MacGyver(map)
        #self.map.add_macgyver(macgyver)
        #self.boss = Boss(map)
        #self.map.add_boss(boss) 
        #self.items = Items()

    def start(self):
        print(level)
            
    #def direction(self):
        
            
                
