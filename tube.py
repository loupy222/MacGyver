from constants import sprite_size, tube
import pygame
from pygame.locals import *

class Tube:

    def __init__ (self, name, structure, position):
        self.name = name
        self.position = position
        self.structure = structure
        self.case_x = position[0]
        self.case_y = position[1]
        self.structure[self.case_x][self.case_y] = "T"
        self.picture = pygame.image.load(tube).convert()
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size