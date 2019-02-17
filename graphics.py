import constants
import labyrinth
import pygame

class main_dysplay:
    #Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
    g_board = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
    #Icone
    icon = pygame.image.load(constants.icon_img)
    pygame.display.set_icon(icon)
    #Titre
    pygame.display.set_caption(constants.Title)
    g_board.blit((0,0))

g_board = main_dysplay()

class HomeLoopDisplay:
    #Home screen
	home = pygame.image.load(constants.home_pic).convert()
	g_board.blit(home, (0,0))

	#Refresh screen
	pygame.display.flip()
"""home_board = Home_loop_display()"""

class GameLoopDisplay:

    #Chargement du fond
	back_img = pygame.image.load(constants.back_img).convert()
	g_board.blit(back_img, (0,0))
	labyrinth.my_lab(g_board)


game_board = GameLoopDisplay ()