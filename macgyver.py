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

	pprint.pprint(labyrinth.my_lab.structure)
	Mac = character.mac
	g_continue = True	

	while g_continue:
	
		#Limitation of loop speed
		#pygame.time.Clock().tick(30)"""

		for event in pygame.event.get():
			pressed = pygame.key.get_pressed()

			if event.type == QUIT:
				game_loop = False

			elif pressed[pygame.K_ESCAPE]:
				g_continue = False

			elif pressed[pygame.K_RIGHT]:
				Mac.moove('rignt')

			elif pressed[pygame.K_LEFT]:
				Mac.moove('left')

			elif pressed[pygame.K_UP]:
				Mac.moove('up')

			elif pressed[pygame.K_DOWN]:
				Mac.moove('down')

	pprint.pprint(labyrinth.my_lab.structure)

	if labyrinth.my_lab.structure[Mac.case_y][Mac.case_x] == 'G':
		print("You win")
		game_loop = False