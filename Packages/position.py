'''A Position class to calculate movements'''
class Position:

    #Initialize position
    def __init__(self, x, y):
        self.position = (x, y)

    #Special method which displays a position as a tuple
    def __repr__(self):
        return str(self.position)

    #Special method which calculates the position hash
    def __hash__(self):
        return hash(self.position)

    #Special method which allows to compare any position in a set 
    def __eq__(self, pos):
        return self.position == pos.position

    #Calculate position to the top
    def up(self):
        x, y = self.position
        return Position(x+1, y)

    #Calculate position to the top
    def down(self):
        x, y = self.position
        return Position(x-1, y)

    #Calculate position to the top
    def right(self):
        x, y = self.position
        return Position(x, y+1)

    #Calculate position to the top
    def left(self):
        x, y = self.position
        return Position(x, y-1)
    
