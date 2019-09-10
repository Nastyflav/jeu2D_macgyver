import os

from position import Position

'''a Map class '''
class Map:

    #Map creation
    def __init__(self, filename):
        self.filename = filename
        #Start
        self._start = set()
        #Exit
        self._exit = set() 
        #Paths
        self._paths = set()
        #Hero
        self.hero = None
        #Boss
        self.boss = None
        #Items
        #Maze dimensions
        self.height = None
        self.width = None
        #File attribut
        self.load_from_file()

    @property
    def start(self):
        return list(self.start)[0]

    #is a position an available path ?
    def available_path(self, position):
        return position in self.paths

    #Loading map
    def load_from_file(self):
        '''Load the file (filename) content into the paths attribut. Identify as well the start and exit positions'''
        with open(self.filename) as infile:
            #Use enumerate in a loop to list every square and its nature
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    #if there is a path square (0 as PATH_CHAR)
                    if col == constants.PATHS_CHAR:
                        self._paths.add(Position, (x, y))
                    #if this is the start square(S as START_CHAR)   
                    elif col == constants.START_CHAR:
                        self._start.add(Position(x, y))
                        self._paths.add(Position(x, y))
                    #if this is the exit square (E as EXIT_CHAR)       
                    elif col == constants.EXIT_CHAR:
                        self._exit.add(Position(x, y))
                        self._paths.add(Position(x, y))
            #
            self.height = x + 1
            self.width = y + 1

    def add_macgyver (self, macgyver):
        '''Position MacGyver in the labyrinth'''
        self.macgyver = macgyver
        #MacGyver start position
        self.macgyver.position = self.start
        #So that MG can communicate with the Map class
        self.macgyver.Map = self

    def add_boss (self, boss):
        '''Position MacGyver in the labyrinth'''
        self.boss = boss
        #Boss start position
        self.boss.position = self.exit
        #So that the boss can communicate with the Map class
        self.boss.Map = self

def main():
    map = Map('Maps/level.txt')

if __name__ =="__main__":
    main()



