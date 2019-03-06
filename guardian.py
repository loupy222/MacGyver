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