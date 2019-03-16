import pygame
from pygame.locals import *
pygame.init()

class GameEvents:
    """
    Class for imput the user keys, and user events.
    """

    def __init__(self, character, window):
        self.character = character
            
        for event in pygame.event.get():                
               
            if event.type == KEYDOWN:                

                if event.key == K_RIGHT:
                    self.character.moove('right')
                    
                elif event.key == K_LEFT:
                    self.character.moove('left')
                   
                elif event.key == K_UP:
                    self.character.moove('up')
                    
                elif event.key == K_DOWN:
                    self.character.moove('down')                

       