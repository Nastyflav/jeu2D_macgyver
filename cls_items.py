#import pygame
#from pygame.locals import * 
#from constants import *
    
class Equipment:

    def __init__(self, position):

        #sprites item ?
        #item position
            #randomly dispatched
            #only on available square
            #can't be on the same square than another item
    
    #item actions
    def item_action
        #if MC walks on it
            #not on the screen anymore
            #appears on the equipment counter
        #else stay where it is

class Needle(Equipment):

    #needle initialization
    def _init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load("aiguille.png").convert_alpha()

class Plastic_tube(Equipment):

    #plastic tube initialization
    def __init__ (self, image, position):
        super().__init__()
        self.image = pygame.image.load("tube_plastique.png").convert_alpha()

class Ether(Equipment):

    #ether initialization
    def __init__ (self, image, position):
        super().__init__()
        pygame.image.load("ether.png").convert_alpha()
