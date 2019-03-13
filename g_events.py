import pygame.event as event

class GameEvents:
    """
    Class for imput the user keys, and user events.
    """

    def __init__(self, character):
        self.character = character
       
    def g_controls (self):
            
        for event in event.get():                
                   
            if event.type == pygame.QUIT:
                break
                
            elif event.type == pygame.KEYDOWN:                       
                if event.key == pygame.K_ESCAPE:
                    break
            elif event.key == pygame.K_RIGHT:
                self.character.moove('right')
            elif event.key == pygame.K_LEFT:
                self.character.moove('left')
            elif event.key == pygame.K_UP:
                self.character.moove('up')
            elif event.key == pygame.K_DOWN:
                self.character.moove('down')			
