from pygame import event


class GameEvents:

    def __init__(self, character):
        self.character = character
       
    def choice (self):

        for event in event.get():
                
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                #choice = 0
                game_loop = False
                        
            elif event.type == KEYDOWN:				
                    
                    if event.key == K_ENTER:
                        choice = 0


    def g_controls (self):
            
        for event in event.get():                
                   
            if event.type == QUIT:
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
