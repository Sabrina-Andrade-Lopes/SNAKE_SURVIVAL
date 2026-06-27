#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from const import *


class Score:
    """
    Responsável pelo controle da pontuação do jogo.
    """

    def __init__(self):
        """
        Inicializa a pontuação.
        """

        self.points = 0

        self.font = pygame.font.SysFont(
            FONT_NAME,
            FONT_SIZE
        )

    def add_point(self):
        """
        Adiciona um ponto à pontuação.
        """

        self.points += 1

    def get_points(self):
        """
        Retorna a pontuação atual.
        """

        return self.points

    def reset(self):
        """
        Reinicia a pontuação.
        """

        self.points = 0

    def draw(self, window):
        """
        Desenha a pontuação na tela.
        """

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