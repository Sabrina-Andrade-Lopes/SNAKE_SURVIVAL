#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import pygame

from entity import Entity
from const import *


class Food(Entity):
    """
    Classe responsável pela comida da cobra.
    """

    def __init__(self):
        """
        Inicializa a comida.
        """

        super().__init__()

        self.color = COLOR_RED

    def spawn(self, snake):
        """
        Gera uma nova posição aleatória para a comida,
        evitando que apareça sobre a cobra.
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

    def reset(self, snake):
        """
        Reinicia a posição da comida.
        """

        self.spawn(snake)

    def draw(self, window):
        """
        Desenha a comida.
        """

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