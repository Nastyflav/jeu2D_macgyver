#import pygame
#from pygame.locals import * 
#from constants import *

class MacGyver: 

    #character initialization
    def __init__ (self, image, position):
        #character image
        self.image = pygame.image.load("MacGyver.png").convert_alpha()
        #position character
        self.position_x = 1
        self.position_y = 3

    #character moves
    def moves (self, direction):    

        #if right direction
        if direction == "right":
            #if MC stays on screen
                #if destination square isn't a wall
                    #one square move
                  

        #if left direction
        if direction == "left":
            #if MC stays on screen
                #if destination square isn't a wall
                    #one square move
                    #position
        
        #if up direction
        if direction == "up":
            #if MC stays on screen
                #if destination square isn't a wall
                    #one square move
                    #position

        #if down direction
        if direction == "up":
            #if MC stays on screen
                #if destination square isn't a wall
                    #one square move
                    #position

