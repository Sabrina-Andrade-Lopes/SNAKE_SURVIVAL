#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import pygame

from Entity import Entity
from const import *


class Food(Entity):

    def __init__(self):
        """
        Inicializa a comida.
        """

        super().__init__()

        self.color = COLOR_RED

        self.x = 0
        self.y = 0

    def spawn(self, snake):
        """
        Gera uma nova posição aleatória para a comida,
        evitando que ela apareça sobre a cobra.
        """

        while True:

            self.x = random.randrange(
                0,
                WIN_WIDTH,
                CELL_SIZE
            )

            self.y = random.randrange(
                0,
                WIN_HEIGHT,
                CELL_SIZE
            )

            if (self.x, self.y) not in snake.body:
                break

    def draw(self, window):
        """
        Desenha a comida na tela.
        """

        if self.image is not None:

            window.blit(
                self.image,
                (
                    self.x,
                    self.y
                )
            )

        else:

            pygame.draw.rect(
                window,
                self.color,
                (
                    self.x,
                    self.y,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

    def reset(self, snake):
        """
        Reposiciona a comida para uma nova partida.
        """

        self.spawn(snake)