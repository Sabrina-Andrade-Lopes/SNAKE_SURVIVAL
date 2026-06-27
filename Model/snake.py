#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from Entity import Entity
from const import *


class Snake(Entity):

    def __init__(self):
        """
        Inicializa a cobra.
        """

        super().__init__()

        self.body = [
            (
                WIN_WIDTH // 2,
                WIN_HEIGHT // 2
            )
        ]

        self.direction = RIGHT
        self.speed = FPS

        self.color = COLOR_GREEN

    def move(self):
        """
        Move a cobra uma posição.
        """

        head_x, head_y = self.body[0]

        if self.direction == UP:
            head_y -= CELL_SIZE

        elif self.direction == DOWN:
            head_y += CELL_SIZE

        elif self.direction == LEFT:
            head_x -= CELL_SIZE

        elif self.direction == RIGHT:
            head_x += CELL_SIZE

        self.body.insert(0, (head_x, head_y))
        self.body.pop()

    def grow(self):
        """
        Aumenta o tamanho da cobra.
        """

        self.body.append(self.body[-1])

    def change_direction(self, direction):
        """
        Altera a direção da cobra.
        Impede que ela volte sobre o próprio corpo.
        """

        if direction == UP and self.direction != DOWN:
            self.direction = UP

        elif direction == DOWN and self.direction != UP:
            self.direction = DOWN

        elif direction == LEFT and self.direction != RIGHT:
            self.direction = LEFT

        elif direction == RIGHT and self.direction != LEFT:
            self.direction = RIGHT

    def handle_input(self):
        """
        Lê o teclado.
        """

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.change_direction(UP)

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.change_direction(DOWN)

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.change_direction(LEFT)

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.change_direction(RIGHT)

    def check_food_collision(self, food):
        """
        Verifica colisão com a comida.
        """

        return self.body[0] == (food.x, food.y)

    def check_wall_collision(self):
        """
        Verifica colisão com as paredes.
        """

        x, y = self.body[0]

        if x < 0:
            return True

        if x >= WIN_WIDTH:
            return True

        if y < 0:
            return True

        if y >= WIN_HEIGHT:
            return True

        return False

    def check_self_collision(self):
        """
        Verifica colisão com o próprio corpo.
        """

        head = self.body[0]

        return head in self.body[1:]

    def reset(self):
        """
        Reinicia a cobra.
        """

        self.body = [
            (
                WIN_WIDTH // 2,
                WIN_HEIGHT // 2
            )
        ]

        self.direction = RIGHT

    def get_head(self):
        """
        Retorna a posição da cabeça.
        """

        return self.body[0]

    def get_size(self):
        """
        Retorna o tamanho da cobra.
        """

        return len(self.body)

    def draw(self, window):
        """
        Desenha a cobra.
        """

        if self.image is not None:

            for segment in self.body:

                window.blit(
                    self.image,
                    segment
                )

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