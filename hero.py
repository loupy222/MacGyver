from constants import numb_sprites_side
from pprint import pprint

class Character:
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
        #self.x = 0
        #self.y = 0
        #print(self.case_x, self.case_y)
        
    def moove(self, direction):

        if direction == "right":
            if self.case_x < (numb_sprites_side - 1):
                if self.structure[self.case_x][self.case_y +1] != "w":
                    self.case_y += 1
                    #self.x = self.case_x * constants.sprite_size            
  
        if direction == "left":
            if self.case_x > 0:
                 if self.structure[self.case_x][self.case_y -1] != "w":
                    self.case_y -= 1
                    #self.x = self.case_x * constants.sprite_size
                  
        if direction == "up":
            if self.case_y > 0:
                if self.structure[self.case_x -1][self.case_y] != "w":
                    self.case_x -= 1
                    #self.y = self.case_y * constants.sprite_size
                   

        if direction == "down":
            if self.case_y < (numb_sprites_side -1):
                if self.structure[self.case_x +1][self.case_y] != "w":
                    self.case_x += 1
                    #self.y = self.case_y * constants.sprite_size
         

    def catch_item(self):
        back_pack = []
        if [self.case_x][self.case_y] == "T":
            back_pack.add("tube")
            print("You take ",back_pack, " in your poket!")
        elif [self.case_x][self.case_y] == "S":            
            back_pack.add("syringe")
            print("You have ",back_pack, " in your poket, now!")
        elif [self.case_x][self.case_y] == "P":
            back_pack.add("poison")
            print("You have ",back_pack, " in your poket, dam it's nice!")
        elif len(back_pack) == 3:
            return True
        else:
            return False
