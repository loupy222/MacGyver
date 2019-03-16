from random import randint
from constants import sprite_size, wall_img, departure_img, guardian_img
import pygame
from pygame.locals import * 


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

    def lab_display(self, window):
        """
        This method loads the images from "constants" and place them on structure
        """

        wall = pygame.image.load(wall_img).convert()
        departure = pygame.image.load(departure_img).convert()
        guardian = pygame.image.load(guardian_img).convert()

        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                """x = x * sprite_size
                y = y * sprite_size"""
                if self.structure[x][y] == "D":
                    window.blit(departure, (x,y))
                elif self.structure[x][y] == "w":
                    window.blit(wall, (x,y))
                elif self.structure[x][y] == "A":
                    window.blit(guardian, (x,y))

