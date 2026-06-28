#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from const import *


class EndScreen:

    def __init__(self, window):

        self.window = window

        self.result = GAME_OVER
        self.score = 0

        self.title_font = pygame.font.SysFont(
            FONT_NAME,
            TITLE_FONT_SIZE,
            bold=True
        )

        self.text_font = pygame.font.SysFont(
            FONT_NAME,
            FONT_SIZE
        )

        self.info_font = pygame.font.SysFont(
            FONT_NAME,
            SMALL_FONT_SIZE
        )

    def set_result(self, result, score):

        self.result = result
        self.score = score

    def run(self):

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

        self.window.fill(COLOR_BLACK)

        # Título

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

        self.window.blit(
            title,
            (
                WIN_WIDTH // 2 - title.get_width() // 2,
                END_TITLE_Y
            )
        )

        # Pontuação Final

        score_text = self.text_font.render(
            f"Pontuação Final: {self.score}",
            True,
            COLOR_WHITE
        )

        self.window.blit(
            score_text,
            (
                WIN_WIDTH // 2 - score_text.get_width() // 2,
                END_MESSAGE_Y
            )
        )

        # Opções

        menu_text = self.info_font.render(
            "ENTER - Voltar ao Menu",
            True,
            COLOR_WHITE
        )

        self.window.blit(
            menu_text,
            (
                WIN_WIDTH // 2 - menu_text.get_width() // 2,
                END_MESSAGE_Y + 50
            )
        )

        exit_text = self.info_font.render(
            "ESC - Sair",
            True,
            COLOR_YELLOW
        )

        self.window.blit(
            exit_text,
            (
                WIN_WIDTH // 2 - exit_text.get_width() // 2,
                END_MESSAGE_Y + 80
            )
        )