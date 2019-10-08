#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg

from map import Map
from macgyver import Macgyver
from map_display import Map_display
from Settings.constants import *


class Game:
    
    def __init__(self):
        #Pygame initialization
        pg.init()
        #Pygame functions to create a screen, and to give it a title / icon
        pg.display.set_caption(WINDOW_TITLE)
        self.icon = pg.image.load(ICON).convert_alpha()
        self.screen = pg.display.set_mode((WINDOW_SIZE))
        #Calling the display method
        Map_display.display_map()
        #Uptading display method once every image is set
        pg.display.update()

        self.running = False
        self.clock = pg.time.Clock()

    def start(self):
        self.running = True
        while self.running:

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
