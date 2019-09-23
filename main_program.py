import os

# from Packages.Game import Game
from Packages.Map import Map

def main():
    map = Map('Maps/level.txt')

    map.load_from_file()
    map.map_display()

    # character = Character()

    # map = character.move_right(map)
    # map.display_map()

    
if __name__ =="__main__":
    main()







