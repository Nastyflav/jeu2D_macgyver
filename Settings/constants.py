#! /usr/bin/env python3
# coding: utf-8
import os

#Square size window parameters
SPRITE_NUMBER = 15 #squares maze number
SPRITE_SIZE = 40
SIDE_DIM = SPRITE_NUMBER * SPRITE_SIZE

#Characters of the map text file
START_SQUARE = "M"
EXIT_SQUARE = "B"
PATHS_SQUARE = "."
WALLS_SQUARE = "W"
      
#Window settings
WINDOW_TITLE = "The Great Escape of MacGyver"
ICON = os.path.join ('resources', 'MacGyver.png')

#Images lists
IMAGE_WALL = os.path.join ('resources', 'wall.png')
IMAGE_PATH = os.path.join ('resources', 'path.png')
IMAGE_MACGYVER = os.path.join ('resources', 'MacGyver.png')
IMAGE_BOSS = os.path.join ('resources', 'Gardien.png')
IMAGE_NEEDLE = os.path.join ('resources', 'aiguille.png')
IMAGE_TUBE = os.path.join ('resources', 'tube_plastique.png')
IMAGE_ETHER = os.path.join ('resources', 'ether.png')

#Game frames speed
FPS = 30
