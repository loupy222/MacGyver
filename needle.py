from constants import sprite_size, needle
from pygame import display

class Needle:

    def __init__ (self, name, structure, position):
        self.name = name
        self.position = position
        self.structure = structure
        self.case_x = position[0]
        self.case_y = position[1]
        self.structure[self.case_x][self.case_y] = "N"
        self.picture = pygame.image.load(needle).convert()
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size
