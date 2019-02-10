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
        # To display the structure of labyrinth
        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                position = position(x, y)
                if self.structure[x][y] == "w":
                    window.blit(wall_picture, (position.pixels_x, position.pixels_y))

    # take randomly a free space from the structure []

    def rand_free_tile(self):
        rand_line = random.choice(self.structure)
        rand_free_tile = random.choice(rand_line)
        if rand_free_tile != "w, M, G, T, S, P":
            random.choice(rand_line)
        return rand_free_tile

my_lab = Labyrinth()

pprint.pprint(my_lab.show)
"""
class character:

    def __init__(self):
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.structure = my_lab.structure
    
    def moove(self, direction):

        if direction == "right":
            if self.case_x < (constants.numb_sprites_side - 1):
                if self.structure[self.case_y][self.case_x + 1]!= "w":
                    self.case_x += 1
                    self.x = self.case_x * constants.sprite_size

        if direction == "left":
            if self.case_x > 0:
                 if self.structure[self.case_y][self.case_x - 1]!= "w":
                     self.case_x -= 1
                     self.x = self.case_x * constants.sprite_size

        if direction == "up":
            if self.case_y > 0:
                if self.structure[self.case_y - 1][self.case_x] != "w":
                    self.case_y -= 1
                    self.y = self.case_y * constants.sprite_size

        if direction == "down":
            if self.case_y < (constants.numb_sprites_side -1):
                self.case_y += 1
                self.y = self.case_y * constants.sprite_size

Mac = character()"""