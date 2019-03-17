from constants import numb_sprites_side, sprite_size, mac_img
import pygame
from pygame.locals import *


class Character:
    """
    Class to create the characters whith name,
    initial position, valid mooves and catch items.
    """ 

    def __init__(self, name, structure, position):
        self.nane = name
        self.position = position
        self.structure = structure
        self.case_y = position[0]
        self.case_x = position[1]
        back_pack = ()
        self.back_pack = back_pack
        self.structure[self.case_y][self.case_x] = "M"
        self.picture = pygame.image.load(mac_img).convert_alpha()
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size
        
    def moove(self, direction):

        if direction == "right":           
            if self.case_y < (numb_sprites_side - 1):
                if self.structure[self.case_y +1][self.case_x] != "w":
                    self.case_y += 1
                    self.y = self.case_y * sprite_size            
  
        if direction == "left":
            if self.case_y >0:
                if self.structure[self.case_y -1][self.case_x] != "w":
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size
                  
        if direction == "up": 
            if self.case_x > 0:
                if self.structure[self.case_y][self.case_x -1] != "w":
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size
                   

        if direction == "down":
            if self.case_x < (numb_sprites_side - 1):
                if self.structure[self.case_y][self.case_x +1] != "w":             
                    self.case_x += 1
                    self.x = self.case_x * sprite_size         

    def catch_item(self):

        if self.structure[self.case_y][self.case_x] == "T":
            self.back_pack += ("tube",)
            print("You find ",self.back_pack, " KEEP TI!!")
    
        if self.structure[self.case_y][self.case_x] == "S":            
            self.back_pack += ("syringe",)
            print("You find ",self.back_pack, " In your pocket!! NOW!")

        if self.structure[self.case_y][self.case_x] == "P":
            self.back_pack += ("poison",)
            print("You find ",self.back_pack, " In your pocket, IT'S NICE!")

        if self.structure[self.case_y][self.case_x] == "N":
            self.back_pack += ("needle",)
            print("You find ",self.back_pack, " In your pocket, cool!")

