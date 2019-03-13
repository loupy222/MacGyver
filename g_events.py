import pygame
pygame.init()

class GameEvents:

    def __init__(self, character):
        self.character = character
       
    def g_controls (self):
            
        for event in event.get():                
                   
            if event.type == pygame.QUIT:
                break
                
            elif event.type == KEYDOWN:                       
                if event.key == K_ESCAPE:
                    break
            elif event.key == K_RIGHT:
                character.moove('right')
            elif event.key == K_LEFT:
                character.moove('left')
            elif event.key == K_UP:
                character.moove('up')
            elif event.key == K_DOWN:
                character.moove('down')			
