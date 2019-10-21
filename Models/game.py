#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg

from Models.map import Map
from Models.macgyver import Macgyver
from Models.map_display import MapDisplay
from Settings.constants import SIDE_DIM, WINDOW_TITLE, FPS, ICON, WHITE, BLACK


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
        self.win = self.message.render('YOU WIN ! Press ENTER to restart', True, (WHITE))
        self.lost = self.message.render('YOU LOST ! Press ENTER to restart', True, (WHITE))
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
            #We call every class methods + the map display
            self.display.display_map(self.map, self.screen)
            self.keyboard_events()
            self.items_counter()
            self.clock.tick(FPS)
            self.endings()

    #Method to check if all the items are collected, and printing win or loss messages
    def endings(self):
        #check if Macgyver is in front of the boss
        if self.map.map_array[self.macgyver.y][self.macgyver.x + 1] == 'B':
            #if he got all the items, player wins
            if self.macgyver.items_collected == 3:
                self.rect = pg.draw.rect(self.screen, BLACK, [0, 300, 600, 50])
                self.screen.blit(self.win, (140, 315))
                pg.display.update()
                pg.time.wait(10000)
                self.running = False
                #Player can restart over
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_RETURN:
                            self.running = True
            #if he doesn't have all the items, player loses
            else:
                self.rect = pg.draw.rect(self.screen, BLACK, [0, 300, 600, 50])
                self.screen.blit(self.lost, (140, 315))
                pg.display.update()
                pg.time.wait(10000)
                self.running = False
                #Player can restart over
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_RETURN:
                            self.running = True
                                  
    #Method for keyboard controllers during the game, implemented into the game.start() method  
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

    #Method to display the items counter
    def items_counter(self):
        #Set the items counter
        self.counter_message = pg.font.SysFont(None, 50)
        self.counter = self.counter_message.render('Items : ' + str(self.macgyver.items_collected), True, (WHITE))#call the MG class on the items number
        self.screen.blit(self.counter, (450, 570))
        #Pygame method to update the map display
        pg.display.update()

