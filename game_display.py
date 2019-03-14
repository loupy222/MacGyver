import constants
import pygame
pygame.init()

class GameDisplay:
    """
    Class for create the window and the game structure.
    """
    g_board = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
    icon = pygame.image.load(constants.icon_img)
    pygame.display.set_icon(icon)
    pygame.display.set_caption(constants.Title)
    #g_board.blit((0,0))
    """
    This method loads the images from "constants" and place tehm on 
    """
  
    wall_picture = pygame.image.load(constants.wall).convert()
    guardian_picture = pygame.image.load(constants.guardian).convert()
    poison = pygame.image.load(constants.poison).convert()
    tube = pygame.image.load(constants.tube).convert()
    syringe = pygame.image.load(constants.syringe).convert()
    back_img = pygame.image.load(constants.back_img).convert()
    mac = pygame.image.load(constants.Mac).convert()


    def __init__(self, structure):
        self.structure = structure

    def game_display(self):

        # To display the structure of labyrinth

        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                if self.structure[x][y] == "w":
                    g_board.blit(wall_picture, (position.pixels_x, position.pixels_y))
                elif self.structure[x][y] == "G":
                    g_board.blit(guardian_picture,(position.pixels_x, position.pixels_y))
                elif self.structure[x][y] == "P":
                    g_board.blit(poison, (position.pixels_x, position.pixels_y))
                elif self.structure[x][y] == "S":
                    g_board.blit(syringe, (position.pixels_x, position.pixels_y))
                elif self.structure[x][y] == "T":
                    g_board.blit(tube, (position.pixels_x, position.pixels_y))
                elif self.structure[x][y] == "M":
                    g_board.blit(mac, (poisition.pixels_x, position.pixels_y))
        g_board.blit(back_img, (0,0))
        g_board.blit((0,0))
g = 1       
while g:

    surface = GameDisplay.game_display() 