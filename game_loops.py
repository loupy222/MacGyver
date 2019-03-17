import constants
from labyrinth import Labyrinth
from hero import Character
from guardian import Guardian
from tube import Tube
from syringe import Syringe
from poison import Poison
from needle import Needle
from pprint import pprint
from g_events import GameEvents
import pygame
from pygame.locals import *
pygame.init()


class GameLoops:

    def __init__ (self):
        pass
        """
        Creation of the main window 
        """

        self.window = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
        icon = pygame.image.load(constants.icon_img)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(constants.Title)


        """
        Creation of game structure, characters and items.
        """

    def home_loops (self):
        home_pic = pygame.image.load(constants.home_pic).convert()

        home_loop = True
        game_loop = False
        while home_loop:
            self.window.blit(home_pic, (0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    home_loop = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_loop = False
                        home_loop = True
                    elif event.key != K_ESCAPE:
                        home_loop = False
                        game_loop = True

    def game_loops (self):
        """
        Creation of game structure, characters and items.
        """

        back_ground = pygame.image.load(constants.back_img).convert()
        lab = Labyrinth()
        lab.lab_display(self.window)
        Mac = Character("Mac", lab.structure, lab.chara_s_position())
        guardian = Guardian("Guardian", lab.structure, lab.guardian_s_position())
        tube = Tube("Tube", lab.structure, lab.rand_free_tile())
        syringe = Syringe("Syringe", lab.structure, lab.rand_free_tile())
        poison = Poison("Poison", lab.structure, lab.rand_free_tile())
        needle = Needle("Needle", lab.structure, lab.rand_free_tile())

        game_loop = True

        while game_loop:
            pygame.time.Clock().tick(60)
            lab.lab_display(self.window)
            print(Mac.back_pack)
            lab.structure[Mac.case_y][Mac.case_x] = " "
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_loop = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_loop = False
                    elif event.key == K_DOWN:
                        Mac.moove('right')
                    elif event.key == K_UP:
                        Mac.moove('left')
                    elif event.key == K_LEFT:
                        Mac.moove('up')
                    elif event.key == K_RIGHT:
                        Mac.moove('down')

            if lab.structure[Mac.case_y][Mac.case_x] == "G":
                if len(Mac.back_pack) == 4:
                    print("You win")
                    print("THANK YOU FOR PLAYING")
                    game_loop = False
                if len(Mac.back_pack) != 4:
                    print("YOU LOOSE! THE GUARDIAN KILL YOU!")
                    game_loop = False
    
            self.window.blit(back_ground, (0,0))
            lab.lab_display(self.window)
            self.window.blit(Mac.picture, (Mac.x, Mac.y))
            pygame.display.flip()
            Mac.catch_item()
            lab.structure[Mac.case_y][Mac.case_x] = "M"

Loop = GameLoops()
Home = Loop.home_loops()
Game = Loop.game_loops()