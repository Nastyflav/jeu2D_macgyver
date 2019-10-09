#! /usr/bin/env python3
# coding: utf-8
import os

#Square size window parameters
SPRITE_WIDTH = 15 #squares maze number
SPRITE_HEIGHT = 15
SPRITE_SIZE = 40
WINDOW_SIZE = SPRITE_WIDTH * SPRITE_SIZE
SCREEN_HEIGHT = 860
SCREEN_WIDTH = 860

#Characters of the map text file
START_SQUARE = "M"
EXIT_SQUARE = "B"
PATHS_SQUARE = "."
WALLS_SQUARE = "W"
      
#Window settings
WINDOW_TITLE = "The Great Escape of MacGyver"
ICON = os.path.join ('resources', 'MacGyver.png')

#Images lists
IMAGE_PATHS = os.path.join ('resources', 'floor-tiles-20x20')
IMAGE_WALLS = os.path.join ('resources', 'floor-tiles-20x20')
IMAGE_MACGYVER = os.path.join ('resources', 'MacGyver.png')
IMAGE_BOSS = os.path.join ('resources', 'Gardien.png')
IMAGE_NEEDLE = os.path.join ('resources', 'aiguille.png')
IMAGE_TUBE = os.path.join ('resources', 'tube_plastique.png')
IMAGE_ETHER = os.path.join ('resources', 'ether.png')

#Game frames speed
FPS = 30
