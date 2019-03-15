from constants import sprite_size, guardian

class Guardian:
    """
    Class to create the "Guardian" charater whith name and
    initial position.
    """ 

    def __init__(self, name, structure, position):
        self.nane = name
        self.position = position
        self.structure = structure
        self.case_x = position[0]
        self.case_y = position[1]
        self.structure[self.case_x][self.case_y] = "G"
        self.picture = pygame.image.load(guardian).convert()
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size