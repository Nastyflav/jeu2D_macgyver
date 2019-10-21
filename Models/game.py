#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg

from Models.map import Map
from Models.macgyver import Macgyver
from Models.map_display import MapDisplay
from Settings.constants import SIDE_DIM, WINDOW_TITLE, FPS, ICON


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
        self.message = pg.font.SysFont(None, 30)
        self.win = self.message.render('YOU WIN ! Press ENTER to restart', True, (255, 255, 255))
        self.lost = self.message.render('YOU LOST ! Press ENTER to restart', True, (255, 255, 255))
        #Set the items counter
        self.counter_message = pg.font.SysFont(None, 10)
        self.counter = self.counter_message.render('Items :', True, (255, 255, 255))
        self.screen.blit(self.counter, (500, 500))
        #Loading map, characters and items
        self.map = Map("Maps/level.txt")
        self.display = MapDisplay(map)
        self.macgyver = Macgyver(map)
        
        self.running = False
        self.clock = pg.time.Clock()
    
    #Method which runs the game, with the map display, the keyboard controls and the victory conditions
    def start(self):
        self.running = True
        while self.running:
            
            self.display.display_map(self.map, self.screen)
            
            self.keyboard_events()
            self.items_counter()
            self.clock.tick(FPS)

            #check if Macgyver is in front of the boss
            if self.map.map_array[self.macgyver.y][self.macgyver.x + 1] == 'B':
                #if he got all the items, player wins
                if self.items_number == 3:
                    self.win_center = self.win.get_rect().center
                    self.screen.blit(self.win, self.win_center)
                    #Player can restart over
                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_RETURN:
                                self.running = True
                #if he don't have all the items, player loses
                else:
                    self.lost_center = self.lost.get_rect().center
                    self.screen.blit(self.win, self.win_center)
                    #Player can restart over
                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_RETURN:
                                self.running = True
                    
            
    #Method for keyboard controllers during the game, implemented int the game.start() method  
    def keyboard_events(self):
        for event in pg.event.get():
            #Quit the game if player closes the window
            if event.type == pg.QUIT:
                self.running = False
            #Player uses arrows to move MG, and ESC to quit the game
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.macgyver.move_up(self.map)
                elif event.key == pg.K_DOWN:
                    self.macgyver.move_down(self.map)
                elif event.key == pg.K_RIGHT:
                    self.macgyver.move_right(self.map)
                elif event.key == pg.K_LEFT:
                    self.macgyver.move_left(self.map)
                elif event.type == pg.K_ESCAPE:
                    self.running = False

    def items_counter(self):
        self.items_number = 0
        if self.macgyver.items_collected == True:
            self.items_number += 1
            self.counter = self.counter_message.render('x ' + str(self.items_number), True,(255, 255, 255))


