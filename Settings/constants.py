#! /usr/bin/env python3
# coding: utf-8
"""Module to link the game images to the constants file"""
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
ICON = os.path.join('images', 'MacGyver.png')

#Images lists
IMAGE_WALL = os.path.join('images', 'wall.png')
IMAGE_PATH = os.path.join('images', 'path.png')
IMAGE_MACGYVER = os.path.join('images', 'MacGyver.png')
IMAGE_BOSS = os.path.join('images', 'Gardien.png')
IMAGE_NEEDLE = os.path.join('images', 'aiguille.png')
IMAGE_TUBE = os.path.join('images', 'tube_plastique.png')
IMAGE_ETHER = os.path.join('images', 'ether.png')

#Game frames speed
FPS = 30

#Colors
WHITE = 255, 255, 255
BLACK = 0, 0, 0
