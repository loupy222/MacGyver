from Data.constants import sprite_size

class Syringe:

    def __init__ (self, name, structure, position):
        self.name = name
        self.position = position
        self.structure = structure
        self.case_y = position[0]
        self.case_x = position[1]
        self.structure[self.case_y][self.case_x] = "S"
