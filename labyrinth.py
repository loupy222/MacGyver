import pprint
import constants
import random
import pygame

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

    def show(self, window):
        """
        This method is to display the game board
        """
        wall_picture = pygame.image.load(constants.wall).convert()
        guardian_picture = pygame.image.load(constants.guardian).convert()
        # To display the structure of labyrinth
        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                position = position(x, y)
                if self.structure[x][y] == "w":
                    window.blit(wall_picture, (position.pixels_x, position.pixels_y))
                elif self.structure[x][y] == "G":
                    window.blit(guardian_picture,(position.pixels_x, position.pixels_y))
    # take randomly a free space from the structure []

    def rand_free_tile(self):
        rand_line = random.choice(self.structure)
        rand_free_tile = random.choice(rand_line)
        if rand_free_tile == "w":
            random.choice(rand_line)

my_lab = Labyrinth()

pprint.pprint(my_lab.structure)
my_lab.rand_free_tile()