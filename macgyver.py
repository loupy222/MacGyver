#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Script Python
"""
import os
import labyrinth
from mooves import mooves 
import character
import constants
import pprint

print("BIENVENNU Sur MacGyver Scapes")
game_loop = True

while game_loop:

	lab = labyrinth.my_lab.structure
	g_continue = True	
	pprint.pprint(lab)
	while g_continue:

		Mac = character.mac
		user_answer = input("Quel direction voulez-vous prendre? (up, down, right, left)  ")

		if user_answer == "right":
			Mac.mooves.right()
			pprint.pprint(Mac.structure)
		if user_answer == "left":
			Mac.mooves.left()

		if user_answer == "up":
			Mac.mooves.up()

		if user_answer == "down":
			Mac.mooves.down()

		pprint.pprint(labyrinth.my_lab.structure)

	if labyrinth.my_lab.structure[Mac.case_y][Mac.case_x] == 'G':
		print("You win")
		game_loop = False
		print("MERCI D'AVOIR JOUE")
		g_continue = False

	
os.system("pause")
g_continue = True	