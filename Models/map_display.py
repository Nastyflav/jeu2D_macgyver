#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg

from Models.map import Map
from Settings.constants import *


class Map_display:

    #Display method to print the map into the terminal
    def __init__(self):
        pass
	
	def display_map(self, screen, map):
		#Images loading
	    self.wall = pg.image.load(IMAGE_WALLS).convert()
		self.macgyver = pg.image.load(IMAGE_MACGYVER).convert_alpha()
	    self.boss = pg.image.load(IMAGE_BOSS).convert_alpha()
		self.path = pg.image.load(IMAGE_PATHS).convert()
        self.needle = pg.image.load(IMAGE_NEEDLE).convert_alpha()
        self.tube = pg.image.load(IMAGE_TUBE).convert_alpha()
        self.ether = pg.image.load(IMAGE_ETHER).convert_alpha()

		num_line = 0
		for line in map.map_array:
			num_sprite = 0
			for sprite in line:
				#Calculate the position as pixels
				x = num_sprite * SPRITE_SIZE
				y = num_line * SPRITE_SIZE
				if sprite == 'W':		  
					screen.blit(self.wall, (x, y))
				elif sprite == 'M':		   
					screen.blit(self.macgyver, (x, y))
				elif sprite == 'B':		  
					screen.blit(self.boss, (x, y))
				elif sprite == '.':
					screen.blit(self.path, (x, y))
				num_sprite += 1
			num_line += 1

	# def display_map(self, map):
    #     for line in map.map_array:
    #         for character in line:
    #             print(character, end=" ")
    #         print()