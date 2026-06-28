#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from const import *


class Level:
    """
    Classe responsável pelo controle dos níveis do jogo.
    """

    def __init__(self):
        """
        Inicializa o sistema de níveis.
        """

        self.font = pygame.font.SysFont(
            FONT_NAME,
            FONT_SIZE
        )

        self.reset()

    def update(self, score):
        """
        Atualiza o nível e a velocidade
        de acordo com a pontuação.
        """

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
        """
        Retorna o nível atual.
        """

        return self.current_level

    def get_speed(self):
        """
        Retorna a velocidade correspondente ao nível.
        """

        return self.speed

    def get_target_score(self):
        """
        Retorna a pontuação necessária para vencer.
        """

        return TARGET_SCORE

    def reset(self):
        """
        Reinicia o sistema de níveis.
        """

        self.current_level = LEVEL_1
        self.speed = LEVEL_1_SPEED

    def draw(self, window):
        """
        Desenha o nível atual na tela.
        """

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