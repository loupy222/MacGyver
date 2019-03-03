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
from pprint import pprint



print("BIENVENNU Sur MacGyver Scapes")
game_loop = True
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
Place characters and items in the game structure.
"""
lab.structure[Guardian.case_x][Guardian.case_y] = "G"
lab.structure[syringe.case_x][syringe.case_y] = "S"
lab.structure[tube.case_x][tube.case_y] = "T"
lab.structure[poison.case_x][poison.case_y] = "P"
lab.structure[Mac.case_x][Mac.case_y] = "M"
pprint(lab.structure)

while game_loop:
	lab.structure[0][0] = "D"
	user_answer = input("Quel direction voulez-vous prendre? (up, down, right, left)  ")
	
	lab.structure[Mac.case_x][Mac.case_y] = " "

	if user_answer == "right":
		Mac.moove("right")

	if user_answer == "left":
		Mac.moove("left")

	if user_answer == "up":
		Mac.moove("up")

	if user_answer == "down":
		Mac.moove("down")

	lab.structure[Mac.case_x][Mac.case_y] = "M"
	print(Mac.case_x, Mac.case_y)
	pprint(lab.structure)
	
	"""if lab.structure[Mac.case_y][Mac.case_x] == 'G' and Mac.catch_item == "FULL":
		print("You win")
		game_loop = False
		print("MERCI D'AVOIR JOUE")
		g_continue = False"""

	
os.system("pause")
g_continue = True

if __name__ == "__main__":
    main()