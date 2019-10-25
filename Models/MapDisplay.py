#! /usr/bin/env python3
# coding: utf-8
"""We use Pygame to import images and to blit them on screen"""
import pygame as pg

from Settings.constants import IMAGE_WALL, IMAGE_PATH, IMAGE_MACGYVER, IMAGE_BOSS, \
							IMAGE_NEEDLE, IMAGE_TUBE, IMAGE_ETHER, SPRITE_SIZE



class MapDisplay:
    """Class only used for displaying the game, by loading images and blitting them on the screen"""
    def __init__(self):
        self.wall = pg.image.load(IMAGE_WALL).convert_alpha()
        self.path = pg.image.load(IMAGE_PATH).convert_alpha()
        self.macgyver = pg.image.load(IMAGE_MACGYVER).convert_alpha()
        self.boss = pg.image.load(IMAGE_BOSS).convert_alpha()
        self.needle = pg.image.load(IMAGE_NEEDLE).convert_alpha()
        self.tube = pg.image.load(IMAGE_TUBE).convert_alpha()
        self.ether = pg.image.load(IMAGE_ETHER).convert_alpha()

    def display_map(self, map, screen):
        """Method to analyze the map characters and blit an image on every one of them"""
        line_number = 0
        for line in map.map_array:
            col_number = 0
            for sprite in line:
                x = col_number * SPRITE_SIZE
                y = line_number * SPRITE_SIZE
                if sprite == 'W':
                    screen.blit(self.wall, (x, y))
                elif sprite == 'B':
                    screen.blit(self.path, (x, y))
                    screen.blit(self.boss, (x, y))
                elif sprite == '.':
                    screen.blit(self.path, (x, y))
                elif sprite == 'M':
                    screen.blit(self.path, (x, y))
                    screen.blit(self.macgyver, (x, y))
                elif sprite == 'N':
                    screen.blit(self.path, (x, y))
                    screen.blit(self.needle, (x, y))
                elif sprite == 'T':
                    screen.blit(self.path, (x, y))
                    screen.blit(self.tube, (x, y))
                elif sprite == 'E':
                    screen.blit(self.path, (x, y))
                    screen.blit(self.ether, (x, y))
                col_number += 1
            line_number += 1

	#Method to display the maze into the terminal, before using Pygame graphics
	# def display_terminal(self, map):
	# 	for line in map.map_array:
	# 		for character in line:
	# 			print(character, end=" ")
	# 		print()
