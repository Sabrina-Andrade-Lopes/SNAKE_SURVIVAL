#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from Const import *


class EndScreen:

    def __init__(self, window):

        self.window = window
        self.result = GAME_OVER

        self.title_font = pygame.font.SysFont(
            FONT_NAME,
            TITLE_FONT_SIZE,
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
                    return EXIT

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return MENU

                    elif event.key == pygame.K_ESCAPE:
                        return EXIT

            self.draw()

            pygame.display.update()

    def draw(self):

        self.window.fill(COLOR_BLACK)

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

        message = self.text_font.render(
            "ENTER - Voltar ao Menu",
            True,
            COLOR_WHITE
        )

        self.window.blit(
            message,
            (
                WIN_WIDTH // 2 - message.get_width() // 2,
                END_MESSAGE_Y
            )
        )

        exit_message = self.text_font.render(
            "ESC - Sair",
            True,
            COLOR_YELLOW
        )

        self.window.blit(
            exit_message,
            (
                WIN_WIDTH // 2 - exit_message.get_width() // 2,
                END_MESSAGE_Y + 40
            )
        )