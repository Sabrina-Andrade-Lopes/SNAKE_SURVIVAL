#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from const import *


class EndScreen:
    """
    Tela de fim de jogo (Vitória ou Game Over).
    """

    def __init__(self, window, assets):
        """
        Inicializa a tela final.
        """

        self.window = window
        self.assets = assets

        self.result = GAME_OVER
        self.score = 0

        self.title_font = pygame.font.SysFont(
            FONT_NAME,
            48
        )

        self.text_font = pygame.font.SysFont(
            FONT_NAME,
            FONT_SIZE
        )

    def set_result(self, result, score):
        """
        Define o resultado da partida.
        """

        self.result = result
        self.score = score

    def run(self):
        """
        Executa a tela final.

        ENTER -> Menu
        ESC -> Sair
        """

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return EXIT

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return MENU

                    elif event.key == pygame.K_ESCAPE:
                        return EXIT

            self.draw()

            pygame.display.flip()

    def draw(self):
        """
        Desenha a tela final.
        """

        # Fundo
        self.window.blit(
            self.assets.background_menu,
            (0, 0)
        )

        # Mensagem principal
        if self.result == WIN:

            title = self.title_font.render(
                "VOCÊ VENCEU!",
                True,
                COLOR_GREEN
            )

        else:

            title = self.title_font.render(
                "GAME OVER",
                True,
                COLOR_RED
            )

        title_rect = title.get_rect(
            center=(
                WIN_WIDTH // 2,
                140
            )
        )

        self.window.blit(
            title,
            title_rect
        )

        # Pontuação
        score_text = self.text_font.render(
            f"Pontuação: {self.score}",
            True,
            COLOR_WHITE
        )

        score_rect = score_text.get_rect(
            center=(
                WIN_WIDTH // 2,
                250
            )
        )

        self.window.blit(
            score_text,
            score_rect
        )

        # Voltar ao menu
        menu_text = self.text_font.render(
            "ENTER - Voltar ao Menu",
            True,
            COLOR_WHITE
        )

        menu_rect = menu_text.get_rect(
            center=(
                WIN_WIDTH // 2,
                340
            )
        )

        self.window.blit(
            menu_text,
            menu_rect
        )

        # Sair
        exit_text = self.text_font.render(
            "ESC - Sair",
            True,
            COLOR_WHITE
        )

        exit_rect = exit_text.get_rect(
            center=(
                WIN_WIDTH // 2,
                390
            )
        )

        self.window.blit(
            exit_text,
            exit_rect
        )