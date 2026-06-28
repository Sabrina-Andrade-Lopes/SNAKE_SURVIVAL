#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import pygame

from const import *


def resource_path(relative_path):
    """
    Localiza arquivos tanto no PyCharm quanto
    no executável gerado pelo PyInstaller.
    """

    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ".."
            )
        )

    return os.path.join(base_path, relative_path)


class Assets:

    def __init__(self):

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # ==========================
        # IMAGENS
        # ==========================

        self.background_game = pygame.image.load(
            resource_path("assets/images/background_game.png")
        ).convert()

        self.background_game = pygame.transform.scale(
            self.background_game,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.background_menu = pygame.image.load(
            resource_path("assets/images/background_menu.png")
        ).convert()

        self.background_menu = pygame.transform.scale(
            self.background_menu,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        # ==========================
        # SONS
        # ==========================

        self.eat_sound = pygame.mixer.Sound(
            resource_path("assets/sounds/eat.wav")
        )

        self.game_over_sound = pygame.mixer.Sound(
            resource_path("assets/sounds/game_over.wav")
        )

        # ==========================
        # MÚSICA
        # ==========================

        pygame.mixer.music.load(
            resource_path("assets/sounds/background.mp3")
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