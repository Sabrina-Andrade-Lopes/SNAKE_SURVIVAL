#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from Const import *


class Score:

    def __init__(self):

        self.points = 0

        self.font = pygame.font.SysFont(
            FONT_NAME,
            FONT_SIZE
        )

    def add_point(self):

        self.points += 1

    def get_points(self):

        return self.points

    def reset(self):

        self.points = 0

    def draw(self, window):

        text = self.font.render(
            f"Pontuação: {self.points}/{TARGET_SCORE}",
            True,
            COLOR_WHITE
        )

        window.blit(
            text,
            (
                HUD_MARGIN_X,
                HUD_SCORE_Y
            )
        )