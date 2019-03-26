import pygame
from pygame.locals import *

from Data.constants import numb_sprites_side, sprite_size, mac_img, cool_img, yeah_img, yes_img, syringe_img, tube_img, poison_img, needle_img, backpack_img, full_img

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
            if self.case_y > 0:
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

    def catch_item(self, window):
        tube = pygame.image.load(tube_img).convert_alpha()
        syringe = pygame.image.load(syringe_img).convert_alpha()
        needle = pygame.image.load(needle_img).convert_alpha()
        poison = pygame.image.load(poison_img).convert_alpha()
        backpack = pygame.image.load(backpack_img).convert()
        full = pygame.image.load(full_img).convert_alpha()
        yes = pygame.image.load(yes_img).convert_alpha()
        yeah = pygame.image.load(yeah_img).convert_alpha()
        cool = pygame.image.load(cool_img).convert_alpha()
        window.blit(backpack, (0, 600))

        if self.structure[self.case_y][self.case_x] == "T":
            self.back_pack += ("tube",)
        
        if self.structure[self.case_y][self.case_x] == "S":            
            self.back_pack += ("syringe",)
 
        if self.structure[self.case_y][self.case_x] == "P":
            self.back_pack += ("poison",)

        if self.structure[self.case_y][self.case_x] == "N":
            self.back_pack += ("needle",)

        for elem in self.back_pack:

            if elem == "tube":
                window.blit(tube, (380, 600))
            if elem == "needle":
                window.blit(needle, (420, 600))
            if elem == "poison":
                window.blit(poison, (480, 600))
            if elem == "syringe":
                window.blit(syringe, (520, 600))
            if len(self.back_pack) == 4:
                window.blit(full, (210, 600))
            if len(self.back_pack) == 3:
                window.blit(yes, (210, 600))
            if len(self.back_pack) == 2:
                window.blit(cool, (210, 600))
            if len(self.back_pack) == 1:
                window.blit(yeah, (210, 600))    
