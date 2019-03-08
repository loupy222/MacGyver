#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MAIN GAME PAGE
Script Python
"""

from labyrinth import Labyrinth
from hero import Character
from guardian import Guardian
from items import Items
from pprint import pprint



print("WELCOME TO MACGYVER SCAPES")
game_loop = True
"""
Creation of game structure, characters and items.
"""
lab = Labyrinth()
Mac = Character("Mac", lab.structure, lab.chara_s_position())
Guardian = Guardian("Guardian", lab.structure, lab.guardian_s_position())
tube = Items("Tube", lab.structure, lab.rand_free_tile())
syringe = Items("Syringe", lab.structure, lab.rand_free_tile())
poison = Items("Poison", lab.structure, lab.rand_free_tile())
"""
Place characters and items in the game structure.
"""
lab.structure[Guardian.case_x][Guardian.case_y] = "G"
lab.structure[syringe.case_x][syringe.case_y] = "S"
lab.structure[tube.case_x][tube.case_y] = "T"
lab.structure[poison.case_x][poison.case_y] = "P"
lab.structure[Mac.case_x][Mac.case_y] = "M"
pprint(lab.structure)


while game_loop:
	print(Mac.back_pack)
	lab.structure[Mac.case_x][Mac.case_y] = " "
	user_answer = input("Which direction do you want to take? (up, down, right, left)  ")

	if user_answer == "right":
		Mac.moove("right")

	elif user_answer == "left":
		Mac.moove("left")

	elif user_answer == "up":
		Mac.moove("up")

	elif user_answer == "down":
		Mac.moove("down")

	if lab.structure[Mac.case_x][Mac.case_y] == "G":
		if len(Mac.back_pack) == 3:
			print("You win")
			print("THANK YOU FOR PLAYING")
			game_loop = False
		if len(Mac.back_pack) != 3:
			print("YOU LOOSE! THE GUARDIAN KILL YOU!")
			game_loop = False	
	else:
		Mac.catch_item()
		lab.structure[Mac.case_x][Mac.case_y] = "M"
		print(Mac.case_x, Mac.case_y)
		pprint(lab.structure)


