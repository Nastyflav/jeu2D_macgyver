#! /usr/bin/env python3
# coding: utf-8

"""Only import the Game class to lauch the program"""
from Models.Game import Game


def main():
    """Simple method to lauch the program, by calling the start method of the Game class"""
    game = Game()
    game.start()
if __name__ == "__main__":
    main()
