import constants
import labyrinth

class main_dysplay:
    #Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
    window = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
    #Icone
    icon = pygame.image.load(constants.icon_img)
    pygame.display.set_icon(icon)
    #Titre
    pygame.display.set_caption(constants.Title)

g_board = main_dysplay()

class Home_loop_display:
    #Home screen
	home = pygame.image.load(constants.home_pic).convert()
	window.blit(home, (0,0))

	#Refresh screen
	pygame.display.flip()
home_board = Home_loop_display()

class Game_loop_display:

    #Chargement du fond
	back_img = pygame.image.load(constants.back_img).convert()
	window.blit(back_img, (0,0))
	labyrinth(window)
    """labyrinth = labyrinth.my_lab"""

game_board = Game_loop_display ()