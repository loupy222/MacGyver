#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MAIN GAME PAGE
Script Python
"""

from labyrinth import Labyrinth
from hero import Character
from guardian import Guardian
from tube import Tube
from syringe import Syringe
from poison import Poison
from needle import Needle
from pprint import pprint
from g_events import GameEvents
from lab_display import LabDisplay
import pygame
pygame.init()

"""
Creation of the main window 
 """

g_board = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
icon = pygame.image.load(constants.icon_img)
pygame.display.set_icon(icon)
pygame.display.set_caption(constants.Title)

game_loop = True
"""
Creation of game structure, characters and items.
"""
lab = Labyrinth()
Mac = Character("Mac", lab.structure, lab.chara_s_position())
Guardian = Guardian("Guardian", lab.structure, lab.guardian_s_position())
tube = Tube("Tube", lab.structure, lab.rand_free_tile())
syringe = Syringe("Syringe", lab.structure, lab.rand_free_tile())
poison = Poison("Poison", lab.structure, lab.rand_free_tile())
needle = Needle("Needle", lab.structure, lab.rand_free_tile())


pprint(lab.structure)

while game_loop:
	print(Mac.back_pack)
	lab.structure[Mac.case_x][Mac.case_y] = " "
	print("Which direction do you want to take? (up, down, right, left)  ")

	if lab.structure[Mac.case_x][Mac.case_y] == "G":
		if len(Mac.back_pack) == 4:
			print("You win")
			print("THANK YOU FOR PLAYING")
			game_loop = False
		if len(Mac.back_pack) != 4:
			print("YOU LOOSE! THE GUARDIAN KILL YOU!")
			game_loop = False	
	else:
		Mac.catch_item()
		lab.structure[Mac.case_x][Mac.case_y] = "M"
		print(Mac.case_x, Mac.case_y)
		pprint(lab.structure)

