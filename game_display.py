
import constants
import pygame
pygame.init()

class LabDisplay:
    """
    Class for create the window and the game structure.
    """
    g_board = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
    icon = pygame.image.load(constants.icon_img)
    pygame.display.set_icon(icon)
    pygame.display.set_caption(constants.Title)

    """
    This method loads the images from "constants" and place tehm on 
    """
  
    wall_picture = pygame.image.load(constants.wall).convert()
    back_img = pygame.image.load(constants.back_img).convert()
    


    def __init__(self, structure):
        self.structure = structure

    def lab_display(self, g_board):

        # To display the structure of labyrinth

        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                if self.structure[x][y] == "w":
                    g_board.blit(wall_picture, (position.pixels_x, position.pixels_y))
        g_board.blit(back_img, (0,0))
        g_board.blit((0,0))
g = 1       
while g:

    surface = GameDisplay.game_display() 