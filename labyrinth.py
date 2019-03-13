from random import randint
import constants
import pygame


class Labyrinth:

    def __init__(self):
        """
        This method is to initialize the game board
        from the file "structure" wich contains the structure of the labyrinth,
        and chose ramdomly a free space on the structure
        """
        # Read the file "structure" and save the structure of the labyrinth
        # as a list in structure []

        with open("draw_file",'r') as labyrinth:
            self.structure = [[letter for letter in line if letter != "\n"] for line in labyrinth]


    def rand_free_tile(self):
        rand_line = randint(0, len(self.structure) -1)
        rand_tile = randint(0, len(self.structure[rand_line]) -1)
        rand_free_tile = self.structure[rand_line][rand_tile]
        while rand_free_tile != " ":
            rand_tile = randint(0, len(self.structure[rand_line]) -1)
            rand_free_tile = self.structure[rand_line][rand_tile]
        return rand_line, rand_tile
 
    def chara_s_position(self):    
        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                if self.structure[x][y] == "D":
                    position = x, y
                    return position
    
    def guardian_s_position(self):    
        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                if self.structure[x][y] == "A":
                    position = x, y
                    return position

    def game_display(self):
        """
        This method is to display the game board
        """
        g_board = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
        icon = pygame.image.load(constants.icon_img)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(constants.Title)
        """g_board.blit((0,0))"""   
        wall_picture = pygame.image.load(constants.wall).convert()
        guardian_picture = pygame.image.load(constants.guardian).convert()
        back_img = pygame.image.load(constants.back_img).convert()
	    g_board.blit(back_img, (0,0))
        # To display the structure of labyrinth
        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                position = position(x, y)
                if self.structure[x][y] == "w":
                    g_board.blit(wall_picture, (position.pixels_x, position.pixels_y))
                elif self.structure[x][y] == "G":
                    g_board.blit(guardian_picture,(position.pixels_x, position.pixels_y))