#! /usr/bin/env python3
# coding: utf-8
import os
import pygame as pg

from Models.Game import Game
from Settings.Keyboard import Keyboard
from Settings.constants import *


class Loop:

    def __init__(self):
        self.game = Game()
        self.keyboard = Keyboard()

        self.running = False
        self.clock = pg.time.Clock()
        
    def start(self):
        self.running = True

        while self.running:
            self.clock.tick(FPS)