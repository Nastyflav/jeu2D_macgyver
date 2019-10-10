#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg

from Models.map import Map
from Models.macgyver import Macgyver
from Models.map_display import *
from Settings.constants import *


class Game:
    
    def __init__(self):
        #Pygame initialization
        pg.init()
        pg.font.init()
        #Pygame functions to create a screen, and to give it a title / icon
        self.screen = pg.display.set_mode((SIDE_DIM, SIDE_DIM))
        self.title = pg.display.set_caption(WINDOW_TITLE)
        self.icon = pg.image.load(ICON).convert_alpha()
        pg.display.set_icon(self.icon)

        #Set the end messages : win or lost
        self.message = pg.font.SysFont('Comic Sans MS', 30)
        self.win = self.message.render('YOU WIN !', False, (255,255,255))
        self.lost = self.message.render('YOU LOST !', False, (255,255,255))
        #Loading map, characters and items
        self.macgyver = Macgyver(map)
        self.map = Map("Maps/level.txt")
        self.display = Map_Display(map)

        self.running = False
        self.clock = pg.time.Clock()

    def start(self):
        self.running = True
        while self.running:

            
            #Step 1 : use the map_display method for printing the background
            self.display.display_map(self.map, self.screen)
            #Step 2 : use an update method on every sprites

            #Step 3 : draw what's need to be drawn
            self.keyboard_events()
            
            self.clock.tick(FPS)

            #check if Macgyver is at the end of the maze
            if self.map.map_array[self.macgyver.x][self.macgyver.y] == 'B':
                #if he got all the items, player wins
                if self.macgyver.items_collected == 3:
                    self.win_center = self.win.get_rect().center
                    self.screen.blit(self.win, self.win_center)
                #if he don't have all the items, player loses
                else:
                    self.win_center = self.win.get_rect().center
                    self.screen.blit(self.win, self.win_center)
                    #the game is stopped
                    self.running = False
            
                
    def keyboard_events(self):
        for event in pg.event.get(pg.KEYDOWN):
            if event.key == pg.K_UP:
                self.macgyver.move_up(map)
            elif event.key == pg.K_DOWN:
                self.macgyver.move_down(map)
            elif event.key == pg.K_RIGHT:
                self.macgyver.move_right(map)
            elif event.key == pg.K_LEFT:
                self.macgyver.move_left(map)
            elif event.type == pg.K_ESCAPE:
                self.running = False