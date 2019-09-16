import os

from Packages.Map import Map
from Packages.Position import Position
#from Packages.Macgyver import MacGyver
#from Packages.Boss import Boss
from Settings.constants import *


def main():
    map = Map('Maps/level.txt')
    print(map._exit)
    
    input("Choose your next move")
    
if __name__ =="__main__":
    main()







