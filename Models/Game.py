#! /usr/bin/env python3
# coding: utf-8
"""We import Pygame to create the game screen and the messages"""
import pygame as pg

from Models.Map import Map
from Models.Macgyver import Macgyver
from Models.MapDisplay import MapDisplay
from Settings.constants import SIDE_DIM, WINDOW_TITLE, FPS, ICON, WHITE, BLACK


class Game:
    """Class which coordonates all the classes to create a loop game, and initializes Pygame"""
    
    def __init__(self):
        """Pygame initialization, screen creation and classes calling"""
        pg.init()
        pg.font.init()
    
        self.screen = pg.display.set_mode((SIDE_DIM, SIDE_DIM))
        self.title = pg.display.set_caption(WINDOW_TITLE)
        self.icon = pg.image.load(ICON).convert_alpha()
        pg.display.set_icon(self.icon)
        
        self.message = pg.font.SysFont(None, 30)
        self.win = self.message.render('YOU WIN ! Your syringe puts him to sleep', True, (WHITE))
        self.lost = self.message.render('YOU LOST ! The guardian captured you', True, (WHITE))
        
        self.map = Map("Maps/level.txt")
        self.display = MapDisplay()
        self.macgyver = Macgyver(map)
        
        self.running = False
        self.clock = pg.time.Clock()
    
    def start(self):
        """Method which runs the game, with the map display,
        the keyboard controls and the victory conditions"""
        self.running = True
        while self.running:
            self.display.display_map(self.map, self.screen)
            self.keyboard_events()
            self.items_counter()
            self.clock.tick(FPS)
            self.endings()

    def endings(self):
        """Method called if MG is in front of the boss with or without all the items
        Printing a win or loss message and ending game"""
        if self.map.map_array[self.macgyver.y][self.macgyver.x + 1] == 'B':
            self.rect = pg.draw.rect(self.screen, BLACK, [0, 300, 600, 50])
            if self.macgyver.items_collected == 3:
                self.screen.blit(self.win, (115, 315)) 
            else:
                self.screen.blit(self.lost, (110, 315))
            pg.display.update()
            pg.time.wait(7000)
            self.running = False

    def keyboard_events(self):
        """Method for keyboard controllers during the game, 
        implemented into the game.start() method"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
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
        """Method to display the items counter, 
        by using the Macgyver class to count the items number"""
        self.counter_message = pg.font.SysFont(None, 50)
        self.counter = self.counter_message.render('Items : ' + str(self.macgyver.items_collected), True, (WHITE))
        self.screen.blit(self.counter, (450, 570))
        pg.display.update()
