#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from const import *


class Menu:
    """
    Classe responsável pelo menu principal do jogo.
    """

    def __init__(self, window):
        """
        Inicializa o menu.
        """

        self.window = window

        self.title_font = pygame.font.SysFont(
            FONT_NAME,
            TITLE_FONT_SIZE,
            bold=True
        )

        self.menu_font = pygame.font.SysFont(
            FONT_NAME,
            MENU_FONT_SIZE
        )

        self.info_font = pygame.font.SysFont(
            FONT_NAME,
            SMALL_FONT_SIZE
        )

    def run(self):
        """
        Executa o menu principal.

        Retorna:
            PLAY -> iniciar jogo
            EXIT -> sair do jogo
        """

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return EXIT

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return PLAY

                    elif event.key == pygame.K_ESCAPE:
                        return EXIT

            self.draw()

            pygame.display.flip()

    def draw(self):
        """
        Desenha o menu principal.
        """

        self.window.fill(COLOR_BLACK)

        # -----------------------------
        # Título
        # -----------------------------

        title = self.title_font.render(
            TITLE,
            True,
            COLOR_GREEN
        )

        self.window.blit(
            title,
            (
                WIN_WIDTH // 2 - title.get_width() // 2,
                TITLE_Y
            )
        )

        # -----------------------------
        # Conteúdo do Menu
        # -----------------------------

        lines = [

            "========== CONTROLES ==========",
            "",
            "W ou ↑  - Mover para cima",
            "S ou ↓  - Mover para baixo",
            "A ou ←  - Mover para esquerda",
            "D ou →  - Mover para direita",
            "",
            f"Objetivo: alcançar {TARGET_SCORE} pontos.",
            "",
            "ENTER - Iniciar Jogo",
            "ESC - Sair"

        ]

        y = MENU_START_Y

        for line in lines:

            text = self.menu_font.render(
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

            y += MENU_LINE_SPACING

        # -----------------------------
        # Rodapé
        # -----------------------------

        footer = self.info_font.render(
            "Linguagem de Programação Aplicada - 2026",
            True,
            COLOR_YELLOW
        )

        self.window.blit(
            footer,
            (
                WIN_WIDTH // 2 - footer.get_width() // 2,
                WIN_HEIGHT - 40
            )
        )