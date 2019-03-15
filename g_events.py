import pygame
pygame.init()

class GameEvents:
    """
    Class for imput the user keys, and user events.
    """

    def __init__(self, character):
        self.character = character
       
    def g_controls (self):
            
        for event in pygame.event.get():                
               
            if event.type == KEYDOWN:                

                if event.key == K_RIGHT:
                    self.character.moove('right')
                    break
                elif event.key == K_LEFT:
                    self.character.moove('left')
                    break
                elif event.key == K_UP:
                    self.character.moove('up')
                    break
                elif event.key == K_DOWN:
                    self.character.moove('down')
                    break			
