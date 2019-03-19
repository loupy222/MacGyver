from Data.constants import sprite_size

class Tube:

    def __init__ (self, name, structure, position):
        self.name = name
        self.position = position
        self.structure = structure
        self.case_x = position[0]
        self.case_y = position[1]
        self.structure[self.case_x][self.case_y] = "T"
