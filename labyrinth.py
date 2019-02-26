import pprint
from random import randint


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
        idx = sum(self.structure,[]).index("D")
        idx = idx%15,idx%15
        return idx
    
    def guardian_s_position(self):    
        idx = sum(self.structure,[]).index("A")
        idx = idx%15,idx%15
        return idx


    """def show(self):
        #This method is to display the game board
        wall_picture = pygame.image.load(constants.wall).convert()
        guardian_picture = pygame.image.load(constants.guardian).convert()
        # To display the structure of labyrinth
        for x, line in enumerate(self.structure):
            for y, letter in enumerate(line):
                position = position(x, y)
                if self.structure[x][y] == "w":
                    graphics.g_board.blit(wall_picture, (position.pixels_x, position.pixels_y))
                elif self.structure[x][y] == "G":
                    graphics.g_board.blit(guardian_picture,(position.pixels_x, position.pixels_y))
"""
lab = Labyrinth()