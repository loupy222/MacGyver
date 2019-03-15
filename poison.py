from constants import sprite_size, poison
from pygame import display

class Poison:

    def __init__ (self, name, structure, position):
        self.name = name
        self.position = position
        self.structure = structure
        self.case_x = position[0]
        self.case_y = position[1]
        self.structure[self.case_x][self.case_y] = "P"
        self.picture = pygame.image.load(poison).convert()
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size
