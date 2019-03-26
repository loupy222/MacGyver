#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MAIN GAME PAGE
Script Python
"""

from Data.game_loops import GameLoops

LOOP = GameLoops()
HOME = LOOP.home_loops()
GAME = LOOP.game_loops()

def game():
    """
     Game fonction
    """
    HOME
    GAME
