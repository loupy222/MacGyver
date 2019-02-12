class main_dysplay:
    #Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
    window = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
    #Icone
    icon = pygame.image.load(constants.icon_img)
    pygame.display.set_icon(icon)
    #Titre
    pygame.display.set_caption(constants.Title)

class Home_loop_display:
    	#Home screen
	home = pygame.image.load(constants.home_pic).convert()
	window.blit(home, (0,0))

	#Refresh screen
	pygame.display.flip()

class Game_loop_display:

    #Chargement du fond
		back_img = pygame.image.load(constants.back_img).convert()
		window.blit(back_img, (0,0))
		labyrinth(window)		
		#Création de Macgyver

    labyrinth = labyrinth.my_lab