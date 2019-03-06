class Guardian:
    """
    Class to create the characters whith name,
    initial position, valid mooves and catch items.
    """ 

    def __init__(self, name, structure, position):
        self.nane = name
        self.position = position
        self.structure = structure
        self.case_x = position[0]
        self.case_y = position[1]