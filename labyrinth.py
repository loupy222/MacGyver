import pprint
import constants
import random
import items
import pygame
#import graphics

pygame.init()

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
        rand_line = random.randint(0, len(self.structure) -1)
        print (rand_line)
        rand_tile = random.randint(0, len(self.structure[rand_line]) -1)
        print (rand_tile)
        rand_free_tile = self.structure[rand_line][rand_tile]
        while rand_free_tile != "0":
            rand_tile = random.randint(0, len(self.structure[rand_line]) -1)
            rand_free_tile = self.structure[rand_line][rand_tile]
        return(rand_free_tile)

my_lab = Labyrinth()

pprint.pprint(my_lab.structure)

    """def show(self):
        #This method is to display the game board
        wall_picture = pygame.image.load(constants.wall).convert()
        guardian_picture = pygame.image.load(constants.guardian).convert()
        # To display the structure of labyrinth
        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                position = position(x, y)
                if self.structure[x][y] == "w":
                    graphics.g_board.blit(wall_picture, (position.pixels_x, position.pixels_y))
                elif self.structure[x][y] == "G":
                    graphics.g_board.blit(guardian_picture,(position.pixels_x, position.pixels_y))
    # take randomly a free space from the structure []"""
