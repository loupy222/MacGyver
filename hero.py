
from constants import numb_sprites_side
import pprint


class Character:

    def __init__(self, name, structure, position):
        self.mane = name[0]
        self.position = position
        self.structure = structure
        self.case_x = position[0]
        self.case_y = position[1]
        #self.x = 0
        #self.y = 0
        
    def moove(self, direction):

        if direction == "right":
            if self.case_x < (numb_sprites_side - 1):
                if self.structure[self.case_y] [self.case_x + 1]!= "w":
                    self.case_x += 1
                    #self.x = self.case_x * constants.sprite_size
                   
  
        if direction == "left":
            if self.case_x > 0:
                 if self.structure[self.case_y][self.case_x -1]!= "w":
                    self.case_x -= 1
                    #self.x = self.case_x * constants.sprite_size
                  
        if direction == "up":
            if self.case_y > 0:
                if self.structure[self.case_y -1][self.case_x] != "w":
                    self.case_y -= 1
                    #self.y = self.case_y * constants.sprite_size
                   

        if direction == "down":
            if self.case_y < (numb_sprites_side -1):
                if self.structure[self.case_y +1][self.case_x] != "w":
                    self.case_y += 1
                    #self.y = self.case_y * constants.sprite_size
         

    def catch_item(self, position):
        back_pack = []
        if self.position == macgyver.tube.position:
            back_pack.add("tube")
            print( back_pack )
        elif self.position == macgyver.syringe.position:            
            back_pack.add("syringe")
            print(back_pack )
        elif self.position == macgyver.poison.position:
            back_pack.add("poison")
            print( back_pack)
        elif len(back_pack) == 3:
            return "FULL"
        else:
            return "EMPTY"



#guardian = Character("Guardian", labyrinth.my_lab.guardian_s_position())
