class MacGyver: 

    #character initialization
    def __init__ (self, map):
        #base map
        self.map = map
        #character position / using property from map.py, "start" as an attribut
        self.position = self.map.start

    #character moves
    def moves (self, direction):
        #getattr access an object property using a string
        next_position = getattr(self.position.direction)()
        if next_position in self.map:
            self.position = next_position
        
    #character counter
            #if MG position = item position
                #pick up item
                #implemente counter
                #MG moves
            #else
                #MG moves

