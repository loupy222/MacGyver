import constants

class character:

    def __init__(self):
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.structure = my_lab.structure
    
    def moove(self, direction):

        if direction == "right":
            if self.case_x < (constants.numb_sprites_side - 1):
                if self.structure[self.case_y][self.case_x + 1]!= "w":
                    self.case_x += 1
                    self.x = self.case_x * constants.sprite_size

        if direction == "left":
            if self.case_x > 0:
                 if self.structure[self.case_y][self.case_x - 1]!= "w":
                     self.case_x -= 1
                     self.x = self.case_x * constants.sprite_size

        if direction == "up":
            if self.case_y > 0:
                if self.structure[self.case_y - 1][self.case_x] != "w":
                    self.case_y -= 1
                    self.y = self.case_y * constants.sprite_size

        if direction == "down":
            if self.case_y < (constants.numb_sprites_side -1):
                self.case_y += 1
                self.y = self.case_y * constants.sprite_size

Mac = character()