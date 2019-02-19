import constants
import labyrinth
import items
import pprint

class character:

    def __init__(self):
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.structure = labyrinth.my_lab.structure
        self.position = self.structure.index("S")

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

    def catch_item(self, position):
        back_pack = []
        if self.position == items.tube.position:
            back_pack.append("tube")
        elif self.position == items.syringe.position:
            back_pack.append("syringe")
        elif self.position == items.poison.position:
            back_pack.append("poison")
            
Mac = character()
