from constants as constants
from position import Position

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
        #File attribut
        self.load_from_file()

    @property
    def start(self):
        return list(self.start)[0]

    def available_path(self, position):
        return position in self.paths

    #Loading map
    def load_from_file(self):
        #Level scanning
        with open(self.filename) as infile:
            #Scanning loop
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    #if there is a path square
                    if col == constants.PATHS_CHAR:
                        self._paths.add(Position, (x, y))
                    #if this is the start square    
                    elif col == constants.START_CHAR:
                        self._start.add(Position(x, y))
                        self._paths.add(Position(x, y))
                    #if this is the exit square       
                    elif col == constants.EXIT_CHAR:
                        self._exit.add(Position(x, y))
                        self._paths.add(Position(x, y))

def main():
    map = Map('level.txt')

if __name__ == "__main__"":
    main()
    






