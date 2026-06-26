#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from Const import *


class Level:

    def __init__(self):
        """
        Inicializa o sistema de níveis do jogo.
        """

        self.current_level = LEVEL_1
        self.speed = LEVEL_1_SPEED
        self.target_score = TARGET_SCORE

        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

    def update(self, score):
        """
        Atualiza o nível e a velocidade do jogo
        de acordo com a pontuação.
        """

        if score < LEVEL_2_SCORE:
            self.current_level = LEVEL_1
            self.speed = LEVEL_1_SPEED

        elif score < LEVEL_3_SCORE:
            self.current_level = LEVEL_2
            self.speed = LEVEL_2_SPEED

        elif score < TARGET_SCORE:
            self.current_level = LEVEL_3
            self.speed = LEVEL_3_SPEED

        else:
            # Mantém o último nível quando atingir a pontuação de vitória
            self.current_level = LEVEL_3
            self.speed = LEVEL_3_SPEED

    def get_speed(self):
        """
        Retorna a velocidade atual do jogo.
        """

        return self.speed

    def get_level(self):
        """
        Retorna o nível atual.
        """

        return self.current_level

    def draw(self, window):
        """
        Desenha o nível atual na tela.
        """

        text = self.font.render(
            f"Nível: {self.current_level}",
            True,
            COLOR_WHITE
        )

        window.blit(
            text,
            (
                HUD_MARGIN_X,
                HUD_LEVEL_Y
            )
        )