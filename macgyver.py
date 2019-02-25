#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Script Python
"""
import pygame
from pygame.locals import *
import labyrinth
import character
import constants
import pprint

pygame.init()
"""g_board = graphics.main_dysplay()"""

game_loop = True

while game_loop:


	Mac = character.mac
	moove = character.Character.moove
	pprint.pprint(labyrinth.my_lab.structure)
	g_continue = True	

	while g_continue:
	
		#Limitation of loop speed
		#pygame.time.Clock().tick(30)"""

		"""for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.type == QUIT:
					game_loop = False

				if event.key == K_ESCAPE:
					g_continue = False

				if event.key == K_RIGHT:
					Mac.moove(right)

				if event.key == K_LEFT:
					Mac.moove("left")

				if event.key == K_UP:
					Mac.moove("up")

				if event.key == K_DOWN:
					Mac.moove("down")"""

	pprint.pprint(labyrinth.my_lab.structure)

	if labyrinth.my_lab.structure[Mac.case_y][Mac.case_x] == 'G':
		print("You win")
		game_loop = False