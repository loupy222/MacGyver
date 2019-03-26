import pygame
from pygame.locals import *
import Data.constants
from Data.labyrinth import Labyrinth
from Data.hero import Character
from Data.guardian import Guardian
from Data.item import Item

pygame.init()

class GameLoops:
    """
    Creation of all loops game
    """

    def __init__(self):

        """
        Creation of the main window and game sounds.
        """

        self.window = pygame.display.set_mode((600, 640))
        icon = pygame.image.load(Data.constants.icon_img)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(Data.constants.Title)
        self.sound = pygame.mixer.Sound("sound/Mac.wav")
        self.sound_loose = pygame.mixer.Sound("sound/loose.wav")
        self.sound_win = pygame.mixer.Sound("sound/win.wav")
        self.game_loop = True
        self.home_loop = True

    def home_loops(self):
        """
        Home loop for the welcome window with sound.
        """
        home_pic = pygame.image.load(Data.constants.home_pic).convert()

        self.home_loop = True
        self.game_loop = False
        while self.home_loop:
            self.window.blit(home_pic, (0, 0))
            self.sound.play()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.home_loop = False
                    self.sound.stop()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_loop = False
                        self.home_loop = False
                        pygame.mixer.pause()
                    elif event.key != K_ESCAPE:
                        self.home_loop = False
                        self.game_loop = True
                        pygame.mixer.pause()
            pygame.display.flip()

    def game_loops(self):
        """
        Main game loop
        Creation of game structure, characters and items.
        """
        back_ground = pygame.image.load(Data.constants.back_img).convert_alpha()
        win_img = pygame.image.load(Data.constants.win_img).convert_alpha()
        loose_img = pygame.image.load(Data.constants.youloose_img).convert_alpha()
        lab = Labyrinth()
        lab.lab_display(self.window)
        Mac = Character("Mac", lab.structure, lab.chara_s_position())
        guardian = Guardian("Guardian", lab.structure, lab.guardian_s_position())
        tube = Item("Tube", lab.structure, lab.rand_free_tile())
        syringe = Item("Syringe", lab.structure, lab.rand_free_tile())
        poison = Item("Poison", lab.structure, lab.rand_free_tile())
        needle = Item("Needle", lab.structure, lab.rand_free_tile())

        self.game_loop = True

        while self.game_loop:
            pygame.mixer.unpause()
            self.sound.play(loops=1, maxtime=0, fade_ms=0)
            pygame.time.Clock().tick(60)
            lab.lab_display(self.window)
            lab.structure[Mac.case_y][Mac.case_x] = " "
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_loop = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_loop = False
                    elif event.key == K_DOWN:
                        Mac.moove('right')
                    elif event.key == K_UP:
                        Mac.moove('left')
                    elif event.key == K_LEFT:
                        Mac.moove('up')
                    elif event.key == K_RIGHT:
                        Mac.moove('down')
            pygame.display.flip()

            if lab.structure[Mac.case_y][Mac.case_x] == "G":
                if len(Mac.back_pack) == 4:
                    self.sound.stop()
                    self.game_loop = False
                    win = True
                    while win:
                        self.sound_win.play()
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                win = False
                            elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    win = False
                        self.window.blit(win_img, (0, 0))
                        pygame.display.flip()

                if len(Mac.back_pack) != 4:
                    self.sound.stop()
                    self.game_loop = False
                    loose = True
                    while loose:
                        self.sound_loose.play()
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                loose = False
                            elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    loose = False
                        self.window.blit(loose_img, (0, 0))
                        pygame.display.flip()
    
            self.window.blit(back_ground, (0, 0))
            lab.lab_display(self.window)
            self.window.blit(Mac.picture, (Mac.x, Mac.y))
            Mac.catch_item(self.window)
            lab.structure[Mac.case_y][Mac.case_x] = "M"
            pygame.display.flip()