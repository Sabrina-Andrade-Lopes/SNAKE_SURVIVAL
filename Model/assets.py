#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from const import *


class Assets:

    def __init__(self):

        # Inicializa o mixer caso ainda não esteja iniciado
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # IMAGENS

        self.background_game = pygame.image.load(
            BACKGROUND_GAME
        ).convert()

        self.background_game = pygame.transform.scale(
            self.background_game,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.background_menu = pygame.image.load(
            BACKGROUND_MENU
        ).convert()

        self.background_menu = pygame.transform.scale(
            self.background_menu,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        # SONS

        self.eat_sound = pygame.mixer.Sound(
            EAT_SOUND
        )

        self.game_over_sound = pygame.mixer.Sound(
            GAME_OVER_SOUND
        )

        # MÚSICA

        pygame.mixer.music.load(
            BACKGROUND_MUSIC
        )

        pygame.mixer.music.set_volume(0.30)

    def play_music(self):

        pygame.mixer.music.play(-1)

    def stop_music(self):

        pygame.mixer.music.stop()

    def pause_music(self):

        pygame.mixer.music.pause()

    def resume_music(self):

        pygame.mixer.music.unpause()