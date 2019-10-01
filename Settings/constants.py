#! /usr/bin/env python3
# coding: utf-8
import os

#Game constants

START_SQUARE = "S"
EXIT_SQUARE = "E"
PATHS_SQUARE = "."
WIDTH = 15
HEIGHT = 15
        

#Window settings
#square_number = 15
#sprite_size = 30
#window_size = square_number * sprite_size
WINDOW_TITLE = "The Great Escape of MacGyver"

#Images lists

IMAGE_BACKGROUND = os.path.join ('resources', )
IMAGE_MACGYVER = os.path.join ('resources', 'MacGyver.png')
IMAGE_BOSS = os.path.join ('resources', 'Gardien.png')
IMAGE_NEEDLE = os.path.join ('resources', 'aiguille.png')
IMAGE_TUBE = os.path.join ('resources', 'tube_plastique.png')
IMAGE_ETHER = os.path.join ('resources', 'ether.png')

FPS = 30
