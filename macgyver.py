#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Script Python
"""
import os
import labyrinth
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
		moove = character.Character.moove
		user_answer = input("Quel direction voulez-vous prendre? (up, down, right, left)  ")

		if user_answer == "right":
			Mac.moove("right")
			pprint.pprint(Mac.structure)
		if user_answer == "left":
			Mac.moove("left")

		if user_answer == "up":
			Mac.moove("up")

		if user_answer == "down":
			Mac.moove("down")

		pprint.pprint(labyrinth.my_lab.structure)

	if labyrinth.my_lab.structure[Mac.case_y][Mac.case_x] == 'G':
		print("You win")
		game_loop = False
		quitter = input("Souhaitez-vous me poser une autre question (o/n) ? ")
	else quitter == "n" or quitter == "N":
		print("MERCI D'AVOIR JOUE")
		g_continue = False

	
os.system("pause")
g_continue = True	