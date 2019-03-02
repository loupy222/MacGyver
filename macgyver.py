#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MAIN GAME PAGE
Script Python
"""
import os
from labyrinth import Labyrinth
from hero import Character
from items import Items
import pprint



print("BIENVENNU Sur MacGyver Scapes")
game_loop = True

while game_loop:

	g_continue = True
	"""
	Creation of game structure, characters and items.
	"""
	lab = Labyrinth()

	Mac = Character("Mac", lab.structure, lab.chara_s_position())
	Guardian = Character("Guardian", lab.structure, lab.guardian_s_position())
	tube = Items("Tube", lab.structure, lab.rand_free_tile())
	syringe = Items("Syringe", lab.structure, lab.rand_free_tile())
	poison = Items("Poison", lab.structure, lab.rand_free_tile())
	"""
	Place charatcters and items in the game structure.
	"""
	lab.structure[Mac.case_x][Mac.case_y] = "M"
	lab.structure[Guardian.case_x][Guardian.case_y] = "G"
	lab.structure[syringe.case_x][syringe.case_y] = "S"
	lab.structure[tube.case_x][tube.case_y] = "T"
	lab.structure[poison.case_x][poison.case_y] = "P"

	pprint.pprint(lab.structure)

	
	while g_continue:

		user_answer = input("Quel direction voulez-vous prendre? (up, down, right, left)  ")

		if user_answer == "right":
			Mac.moove("right")
			print(Mac.case_x, Mac.case_y)
		if user_answer == "left":
			Mac.moove("left")
			print(Mac.case_x, Mac.case_y)
		if user_answer == "up":
			Mac.moove("up")
			print(Mac.case_x, Mac.case_y)
		if user_answer == "down":
			Mac.moove("down")
			print(Mac.case_x, Mac.case_y)

		pprint.pprint(lab.structure)

	if lab.structure[Mac.case_y][Mac.case_x] == 'G' and Mac.catch_item == "FULL":
		print("You win")
		game_loop = False
		print("MERCI D'AVOIR JOUE")
		g_continue = False

	
os.system("pause")
g_continue = True	