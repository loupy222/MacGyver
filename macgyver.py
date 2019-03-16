#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MAIN GAME PAGE
Script Python
"""
import constants
from labyrinth import Labyrinth
from hero import Character
from guardian import Guardian
from tube import Tube
from syringe import Syringe
from poison import Poison
from needle import Needle
from pprint import pprint
from g_events import GameEvents
import pygame
pygame.init()

"""
Creation of the main window 
 """

window = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
icon = pygame.image.load(constants.icon_img)
pygame.display.set_icon(icon)
pygame.display.set_caption(constants.Title)
back_ground = pygame.image.load(constants.back_img).convert()

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
g_event = GameEvents
while game_loop:

	pygame.time.Clock().tick(30)

	lab.lab_display(window)
	Mac.picture
	print(Mac.back_pack)
	lab.structure[Mac.case_x][Mac.case_y] = " "
	g_event.g_controls(Mac)


	if lab.structure[Mac.case_x][Mac.case_y] == "G":
		if len(Mac.back_pack) == 4:
			print("You win")
			print("THANK YOU FOR PLAYING")
			game_loop = False
		if len(Mac.back_pack) != 4:
			print("YOU LOOSE! THE GUARDIAN KILL YOU!")
			game_loop = False	
	else:
		window.blit(back_ground, (0,0))
		lab.lab_display(window)
		window.blit(Mac.moove, (Mac.x, Mac.y))
		pygame.display.flip()
		Mac.catch_item()
		lab.structure[Mac.case_x][Mac.case_y] = "M"
		print(Mac.case_x, Mac.case_y)


