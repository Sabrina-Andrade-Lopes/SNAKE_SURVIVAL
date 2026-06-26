#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import pygame

from Entity import Entity
from Const import *


class Food(Entity):

    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = 0

        # Cor temporária (caso não utilize imagem)
        self.color = COLOR_RED

    def spawn(self, snake):

        while True:

            self.x = random.randrange(0, WIN_WIDTH, CELL_SIZE)
            self.y = random.randrange(0, WIN_HEIGHT, CELL_SIZE)

            if (self.x, self.y) not in snake.body:
                break

    def draw(self, window):

        if self.image is not None:

            window.blit(self.image, (self.x, self.y))

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