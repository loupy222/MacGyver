#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Script Python
"""

import labyrinth
import character
import constants
import keyboard
import pprint


"""g_board = graphics.main_dysplay()"""
pprint.pprint(labyrinth.my_lab.structure)
game_loop = True

while game_loop:	

	Mac = character.mac
		
	#Game loop
	"""while g_continue:
	
		#Limitation of loop speed
		#pygame.time.Clock().tick(30)"""
	while True:
		try:
			if keyboard.is_pressed(keyboard.key_RIGHT):
				Mac.moove('rignt')
				break
			else:
				pass
		except:
			break

		try:
			if keyboard.is_pressed(keyboard.KEY_LEFT):
				Mac.moove('left')
				break
			else:
				pass
		except:
			break

		try:
			if keyboard.is_pressed(keyboard.KEY_UP):
				Mac.moove('up')
				break
			else:
				pass
		except:
			break

		try:
			if keyboard.is_pressed(keyboard.KEY_DOWN):
				Mac.moove('down')
				break
			else:
				pass
		except:
			break
		
		"""for event in event.get():

				#Touches de déplacement de macgyver
		if event.type == event.KEYDOWN and event.key == event.K_RIGHT:
			Mac.moove('rignt')

		elif event.type == event.KEYDOWN and event.key == event.K_LEFT:
			Mac.moove('left')

		elif event.type == event.key and event.key == event.K_UP:
			Mac.moove('up')

		elif event.type == event.KEYDOWN and event.key == event.K_DOWN:
			Mac.moove('down')"""


	if labyrinth.my_lab.structure[Mac.case_y][Mac.case_x] == 'G':
		print("You win")
		game_loop = False