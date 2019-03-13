
class Items:

    def __init__ (self, name, structure, position):
        self.name = name[0]
        self.position = position
        self.structure = structure
        self.case_x = self.position[0]
        self.case_y = self.position[1]   

