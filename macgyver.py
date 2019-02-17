"""#!/usr/bin/python3"""
# -*- coding: Utf-8 -*

"""

Script Python

"""

import pygame
import labyrinth
import character
import constants


pygame.init()

g_board = graphics.main_dysplay()

game_loop = True

while game_loop:	
	g_continue = True
	g_home = True

	#Home loop
	while g_home:
		home_board = graphics.Home_loop_display()
		pygame.time.Clock().tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_loop = False
				g_home = False

			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
				game_loop = False
				g_home = False
				g_continue = False
						
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ENTER:				
				g_home = False	#On quitte l'accueil
				g_continue = True

	#on vérifie que le joueur a bien choix de jouer
	#pour ne pas charger s'il quitte
	if g_continue == True:

		#Création de Macgyver
		Mac = character.Mac
				
	#Game loop
	while g_continue:
	
		#Limitation of loop speed
		pygame.time.Clock().tick(30)
		
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == pygame.QUIT:
				g_continue = False
				game_loop = False
			elif event.type == pygame.KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == pygame.K_ESCAPE:
					game_loop = False
					
				#Touches de déplacement de macgyver
				elif event.key == pygame.K_RIGHT:
					Mac.moove('rignt')
				elif event.key == pygame.K_LEFT:
					Mac.moove('left')
				elif event.key == pygame.K_UP:
					Mac.moove('up')
				elif event.key == pygame.K_DOWN:
					Mac.moove('down')			
			
		"""Affichages aux nouvelles positions
		window.blit(back_img, (0,0))
		labyrinth(window)		
		pygame.display.flip()"""

		#Victoire -> Retour à l'accueil
		if labyrinth.my_lab.structure[Mac.case_y][Mac.case_x] == 'G':
			game_loop = False