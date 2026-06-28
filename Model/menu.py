#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from const import *


class Menu:
    """
    Tela inicial do jogo.
    """

    def __init__(self, window, assets):

        self.window = window
        self.assets = assets

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

        self.clock = pygame.time.Clock()

    def run(self):

        running = True

        while running:

            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return EXIT

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return PLAY

                    if event.key == pygame.K_ESCAPE:
                        return EXIT

            self.draw()

            pygame.display.flip()

    def draw(self):

        # -------------------------
        # Fundo do menu
        # -------------------------

        self.window.blit(
            self.assets.background_menu,
            (0, 0)
        )

        # -------------------------
        # Título
        # -------------------------

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

        # -------------------------
        # Opções
        # -------------------------

        options = [

            "PRESSIONE ENTER PARA JOGAR",

            "",

            "CONTROLES",

            "W ou ↑  - Cima",

            "S ou ↓  - Baixo",

            "A ou ←  - Esquerda",

            "D ou →  - Direita",

            "",

            f"OBJETIVO: FAZER {TARGET_SCORE} PONTOS",

            "",

            "ESC - SAIR"

        ]

        y = MENU_START_Y

        for option in options:

            color = COLOR_WHITE

            if option == "CONTROLES":
                color = COLOR_YELLOW

            elif "ENTER" in option:
                color = COLOR_GREEN

            elif "ESC" in option:
                color = COLOR_RED

            text = self.menu_font.render(
                option,
                True,
                color
            )

            self.window.blit(
                text,
                (
                    WIN_WIDTH // 2 - text.get_width() // 2,
                    y
                )
            )

            y += MENU_LINE_SPACING

        # -------------------------
        # Rodapé
        # -------------------------

        footer = self.info_font.render(
            "Linguagem de Programação Aplicada",
            True,
            COLOR_WHITE
        )

        self.window.blit(
            footer,
            (
                WIN_WIDTH // 2 - footer.get_width() // 2,
                FOOTER_Y
            )
        )