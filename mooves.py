import constants
import labyrinth
class mooves:

    def __init__(self):
        self.structure = labyrinth.my_lab.structure
        self.case_x = 0
        self.case_y = 0

    def right(self):
        if self.case_x < (constants.numb_sprites_side -1):
            if self.structure[self.case_x + 1][self.case_y]!= "w":
                return self.structure[self.case_x + 1][self.case_y]

    def left(self):
        if self.case_x > 0:
            if self.structure[self.case_x -1][self.case_y] != "w":
                return self.structure[self.case_x -1][self.case_y]

    def up(self):
        if self.case_y > 0:
            if self.structure[self.case_x][self.case_y -1] != "w":
                return self.structure[self.case_x][self.case_y -1]

    def down(self):
        if self.case_y < (constants.numb_sprites_side -1):
            if self.structure[self.case_x][self.case_y +1] != "w":
                return self.structure[self.case_x][self.case_y +1]

       