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

        self.clock = pygame.time.Clock()

    def run(self):
        """
        Executa o menu.

        Retorna:
            PLAY -> iniciar jogo
            EXIT -> fechar aplicação
        """

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
        """
        Desenha o menu principal.
        """

        self.window.fill(COLOR_BLACK)

        # ==========================
        # Título
        # ==========================

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

        # ==========================
        # Opções do Menu
        # ==========================

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

        # ==========================
        # Rodapé
        # ==========================

        footer = self.info_font.render(
            "Linguagem de Programação Aplicada - Snake Survival",
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