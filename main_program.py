from Packages.Map_cls import Map
from Packages.Position_cls import Position
from Settings.constants import *


def main():
    map = Map('Maps/level.txt')
    print(map._paths)
    input("Choose your next move")
    
if __name__ =="__main__":
    main()







