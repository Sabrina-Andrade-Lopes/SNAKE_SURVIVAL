#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from Entity import Entity
from Const import *


class Snake(Entity):

    def __init__(self):
        super().__init__()

        # Cabeça
        self.x = 200
        self.y = 200

        # Corpo
        self.body = [(self.x, self.y)]

        # Direção inicial
        self.direction = RIGHT

        # Velocidade inicial
        self.speed = FPS

        # Cor temporária
        self.color = COLOR_GREEN

    def move(self):

        if self.direction == UP:
            self.y -= CELL_SIZE

        elif self.direction == DOWN:
            self.y += CELL_SIZE

        elif self.direction == LEFT:
            self.x -= CELL_SIZE

        elif self.direction == RIGHT:
            self.x += CELL_SIZE

        # Atualiza a cabeça
        self.body.insert(0, (self.x, self.y))

        # Remove a cauda
        self.body.pop()

    def grow(self):

        self.body.append(self.body[-1])

    def change_direction(self, direction):

        if direction == UP and self.direction != DOWN:
            self.direction = direction

        elif direction == DOWN and self.direction != UP:
            self.direction = direction

        elif direction == LEFT and self.direction != RIGHT:
            self.direction = direction

        elif direction == RIGHT and self.direction != LEFT:
            self.direction = direction

    def check_self_collision(self):

        return (self.x, self.y) in self.body[1:]

    def draw(self, window):

        if self.image is not None:

            for segment in self.body:
                window.blit(self.image, segment)

        else:

            for segment in self.body:
                pygame.draw.rect(
                    window,
                    self.color,
                    (
                        segment[0],
                        segment[1],
                        CELL_SIZE,
                        CELL_SIZE
                    )
                )