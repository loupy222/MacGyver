#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Script Python
"""
import os
from labyrinth import Labyrinth
import character
import constants
import pprint
from items import Items

print("BIENVENNU Sur MacGyver Scapes")
game_loop = True

while game_loop:

	lab = Labyrinth()
	g_continue = True	
	Mac = character.Character("Mac", lab.chara_s_position())
	Guardian = character.Character("Guardian", lab.guardian_s_position())
	tube = Items("Tube", lab.rand_free_tile())
	syringe = Items("Syringe", lab.rand_free_tile())
	poison = Items("Poison", lab.rand_free_tile())
	pprint.pprint(lab.structure)
	
	while g_continue:

		user_answer = input("Quel direction voulez-vous prendre? (up, down, right, left)  ")

		if user_answer == "right":
			Mac.moove("right")
			pprint.pprint(lab.structure)
		if user_answer == "left":
			Mac.moove("left")

		if user_answer == "up":
			Mac.moove("up")

		if user_answer == "down":
			Mac.moove("down")

		pprint.pprint(lab.structure)

	if labyrinth.my_lab.structure[Mac.case_y][Mac.case_x] == 'G':
		print("You win")
		game_loop = False
		print("MERCI D'AVOIR JOUE")
		g_continue = False

	
os.system("pause")
g_continue = True	