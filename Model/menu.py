#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from Const import *


class Menu:

    def __init__(self, window):

        self.window = window

        self.title_font = pygame.font.SysFont(
            FONT_NAME,
            48,
            bold=True
        )

        self.text_font = pygame.font.SysFont(
            FONT_NAME,
            FONT_SIZE
        )

    def run(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return "EXIT"

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return "PLAY"

                    elif event.key == pygame.K_ESCAPE:
                        return "EXIT"

            self.draw()

            pygame.display.update()

    def draw(self):

        self.window.fill(COLOR_BLACK)

        title = self.title_font.render(
            TITLE,
            True,
            COLOR_GREEN
        )

        self.window.blit(
            title,
            (
                WIN_WIDTH // 2 - title.get_width() // 2,
                50
            )
        )

        lines = [

            "=== CONTROLES ===",
            "",
            "W ou ↑ : Cima",
            "S ou ↓ : Baixo",
            "A ou ← : Esquerda",
            "D ou → : Direita",
            "",
            f"Objetivo: Alcancar {TARGET_SCORE} pontos",
            "",
            "ENTER - Jogar",
            "ESC - Sair"

        ]

        y = 160

        for line in lines:

            text = self.text_font.render(
                line,
                True,
                COLOR_WHITE
            )

            self.window.blit(
                text,
                (
                    WIN_WIDTH // 2 - text.get_width() // 2,
                    y
                )
            )

            y += 35