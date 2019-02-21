import constants
import labyrinth
import items
import pprint

class Character:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.structure = labyrinth.my_lab.structure
        self.structure[position[0]] [position[1]] = name[0]
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

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
                if self.structure[self.case_y + 1][self.case_x] != "w":
                    self.case_y += 1
                    self.y = self.case_y * constants.sprite_size

    def catch_item(self, position):
        back_pack = []
        if self.position == items.tube.position:
            back_pack.append("tube")
            print(back_pack)
        elif self.position == items.syringe.position:            
            back_pack.append("syringe")
            print(back_pack)
        elif self.position == items.poison.position:
            back_pack.append("poison")
            print(back_pack)
        if len(back_pack) == 3:
            return True
        else:
            return False

mac = Character("Mac", labyrinth.my_lab.chara_s_position())
guardian = Character("Guardian", labyrinth.my_lab.guardian_s_position())
"""pprint.pprint(labyrinth.my_lab.structure)"""
