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

    # def display_map(self, map):
    #     for line in map.map_array:
    #         for character in line:
    #             print(character, end=" ")
    #         print()

    def display_map(self, surface):
		#Images loading
	    self.wall = pg.image.load(IMAGE_WALLS).convert()
	    self.macgyver = pg.image.load(IMAGE_MACGYVER).convert_alpha()
	    self.boss = pg.image.load(IMAGE_BOSS).convert_alpha()
        self.paths = pg.image.load(IMAGE_PATHS).convert()
        self.needle = pg.image.load(IMAGE_NEEDLE).convert_alpha()
        self.tube = pg.image.load(IMAGE_TUBE).convert_alpha()
        self.ether = pg.image.load(IMAGE_ETHER).convert_alpha()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for x, line in map.map_array:
			#On parcourt les listes de lignes
			num_case = 0
			for y, col in line:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if col == 'W':		  
					surface.blit(self.wall, (x,y))
				elif col == 'M':		   
					surface.blit(self.macgyver, (x,y))
				elif col == 'B':		  
					surface.blit(self.boss, (x,y))
				num_case += 1
			num_ligne += 1


class Macgyver_display(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.image.load(IMAGE_MACGYVER).convert_alpha()
        self.rect = self.image.get_rect()