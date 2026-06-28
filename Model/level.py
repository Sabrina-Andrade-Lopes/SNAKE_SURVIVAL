#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from const import *


class Level:

    def __init__(self):

        self.font = pygame.font.SysFont(
            FONT_NAME,
            FONT_SIZE
        )

        self.reset()

    def update(self, score):

        if score < LEVEL_2_SCORE:

            self.current_level = LEVEL_1
            self.speed = LEVEL_1_SPEED

        elif score < LEVEL_3_SCORE:

            self.current_level = LEVEL_2
            self.speed = LEVEL_2_SPEED

        else:

            self.current_level = LEVEL_3
            self.speed = LEVEL_3_SPEED

    def get_level(self):

        return self.current_level

    def get_speed(self):

        return self.speed

    def get_target_score(self):

        return TARGET_SCORE

    def reset(self):

        self.current_level = LEVEL_1
        self.speed = LEVEL_1_SPEED

    def draw(self, window):

        level_text = self.font.render(
            f"Nível: {self.current_level}",
            True,
            COLOR_WHITE
        )

        window.blit(
            level_text,
            (
                HUD_MARGIN_X,
                HUD_LEVEL_Y
            )
        )