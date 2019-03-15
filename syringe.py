from constants import sprite_size, syringe

class Syringe:

    def __init__ (self, name, structure, position):
        self.name = name
        self.position = position
        self.structure = structure
        self.case_x = position[0]
        self.case_y = position[1]
        self.structure[self.case_x][self.case_y] = "S"
        self.picture = pygame.image.load(syringe).convert()
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size