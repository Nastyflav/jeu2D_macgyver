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
        #Pygame methods to create screen, to give it a title and and to adjust an image on it
        pg.display.set_caption(WINDOW_TITLE)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.background = pg.image.load(IMAGE_BACKGROUND).convert()
        self.screen.blit(self.background, (0, 0))

        self.sprites = pg.sprite.RenderUpdates()
        self.sprites.add(Macgyver())

        self.macgyver = pg.image.load(IMAGE_MACGYVER).convert_alpha()
        self.screen.blit(self.macgyver)
        #Uptading display method once every image is set
        pg.display.update()

        self.running = False
        self.clock = pg.time.Clock()

    def start(self):
        self.running = True
        while self.running:

            self.sprites.clear(self.screen, self.background)

            self.sprites.update()



            self.keyboard_events()
            
            self.clock.tick(FPS)
            for event in pg.event.get():
                


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
