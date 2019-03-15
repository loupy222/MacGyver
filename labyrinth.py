from random import randint
import constants


class Labyrinth:

    def __init__(self):
        """
        This method is to initialize the game board
        from the file "structure" wich contains the structure of the labyrinth,
        and chose ramdomly a free space on the structure
        """
        # Read the file "structure" and save the structure of the labyrinth
        # as a list in structure []

        with open("draw_file",'r') as labyrinth:
            self.structure = [[letter for letter in line if letter != "\n"] for line in labyrinth]


    def rand_free_tile(self):
        rand_line = randint(0, len(self.structure) -1)
        rand_tile = randint(0, len(self.structure[rand_line]) -1)
        rand_free_tile = self.structure[rand_line][rand_tile]
        while rand_free_tile != " ":
            rand_tile = randint(0, len(self.structure[rand_line]) -1)
            rand_free_tile = self.structure[rand_line][rand_tile]
        return rand_line, rand_tile
 
    def chara_s_position(self):    
        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                if self.structure[x][y] == "D":
                    position = x, y
                    return position
    
    def guardian_s_position(self):    
        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                if self.structure[x][y] == "A":
                    position = x, y
                    return position

