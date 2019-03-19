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
    """
    Creation of all loops game
    """

    def __init__ (self):

        """
        Creation of the main window 
        """

        self.window = pygame.display.set_mode((constants.window_side_size, constants.window_side_size))
        icon = pygame.image.load(constants.icon_img)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(constants.Title)
        self.sound = pygame.mixer.Sound("sound/Mac.wav")
        self.sound_loose = pygame.mixer.Sound("sound/loose.wav")
        self.sound_win = pygame.mixer.sound("sound/win.wav")
    def home_loops (self):
        """
        Home loop for the welcome window
        """
        home_pic = pygame.image.load(constants.home_pic).convert()

        home_loop = True
        game_loop = False
        while home_loop:
            self.window.blit(home_pic, (0,0))
            self.sound.play()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    home_loop = False
                    self.sound.stop()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_loop = False
                        home_loop = True
                        pygame.mixer.pause()
                    elif event.key != K_ESCAPE:
                        home_loop = False
                        game_loop = True
                        pygame.mixer.pause()

    def game_loops (self):
        """
        Main game loop
        Creation of game structure, characters and items.
        """

        back_ground = pygame.image.load(constants.back_img).convert_alpha()
        win_img = pygame.image.load(constants.win_img).convert_alpha()
        loose_img = pygame.image.load(constants.youloose_img).convert_alpha()
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
            pygame.display.flip()
            pygame.mixer.unpause()
            self.sound.play(loops=1, maxtime=0, fade_ms=0)
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
                    self.sound.stop()
                    game_loop = False
                    win = True
                    while win:
                        self.sound_win.play()
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                win = False
                            elif event.type == KEYDOWN:
                                if event.key != K_ESCAPE:
                                    win = False
                        self.window.blit(win_img, (0,0))
                        pygame.display.flip()

                if len(Mac.back_pack) != 4:
                    self.sound.stop()
                    game_loop = False
                    loose = True
                    while loose:
                        self.sound_loose.play()
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                loose = False
                            elif event.type == KEYDOWN:
                                if event.key != K_ESCAPE:
                                    loose = False
                        self.window.blit(loose_img, (0,0))
                        pygame.display.flip()

                    print("YOU LOOSE! THE GUARDIAN KILL YOU!")
    
            self.window.blit(back_ground, (0,0))
            lab.lab_display(self.window)
            self.window.blit(Mac.picture, (Mac.x, Mac.y))
            Mac.catch_item(self.window)
            lab.structure[Mac.case_y][Mac.case_x] = "M"

Loop = GameLoops()
Home = Loop.home_loops()
Game = Loop.game_loops()