#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg

from Models.map import Map
from Models.macgyver import Macgyver
from Models.map_display import Map_Display
from Settings.constants import *


class Game:
    
    def __init__(self):
        #Pygame initialization
        pg.init()
        #Pygame functions to create a screen, and to give it a title / icon
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.title = pg.display.set_caption(WINDOW_TITLE)
        self.icon = pg.image.load(ICON).convert_alpha()
        pg.display.set_icon(self.icon)
        self.background = pg.image.load(IMAGE_BOSS).convert()
        self.screen.blit(self.background, (0, 0))
        #Method to update the screen
        pg.display.update()
        #Loading map, characters and items
        self.map = Map("Maps/level.txt")
        self.map.load_from_file()
        # self.map_display = Map_Display()
        
        #Uptading display method once every image is set
        pg.display.update()

        self.running = False
        self.clock = pg.time.Clock()

    def start(self):
        self.running = True
        while self.running:


            #Step 1 : use the map_display method for printing the background

            #Step 2 : use an update method on every sprites

            #Step 3 : draw what's need to be drawn
            self.keyboard_events()
            
            self.clock.tick(FPS)
                
    def keyboard_events(self):
        for event in pg.event.get(pg.KEYDOWN):
            if event.key == pg.K_UP:
                self.macgyver.move_up()
            elif event.key == pg.K_DOWN:
                self.macgyver.move_down()
            elif event.key == pg.K_RIGHT:
                self.macgyver.move_right()
            elif event.key == pg.K_LEFT:
                self.macgyver.move_left()
            elif event.type == pg.K_ESCAPE:
                self.running = False