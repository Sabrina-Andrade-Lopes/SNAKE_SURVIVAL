#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from entity import Entity
from const import *


class Snake(Entity):

    def __init__(self):

        super().__init__()

        self.reset()

    def reset(self):

        self.body = [
            (5 * CELL_SIZE, 5 * CELL_SIZE),
            (4 * CELL_SIZE, 5 * CELL_SIZE),
            (3 * CELL_SIZE, 5 * CELL_SIZE)
        ]

        self.direction = INITIAL_DIRECTION

        self.next_direction = INITIAL_DIRECTION

        self.speed = LEVEL_1_SPEED

    def handle_input(self):

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.direction != DOWN:
            self.next_direction = UP

        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.direction != UP:
            self.next_direction = DOWN

        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.direction != RIGHT:
            self.next_direction = LEFT

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.direction != LEFT:
            self.next_direction = RIGHT

    def move(self):

        self.direction = self.next_direction

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

        self.body.append(self.body[-1])

    def change_direction(self, direction):

        if direction == UP and self.direction != DOWN:
            self.next_direction = UP

        elif direction == DOWN and self.direction != UP:
            self.next_direction = DOWN

        elif direction == LEFT and self.direction != RIGHT:
            self.next_direction = LEFT

        elif direction == RIGHT and self.direction != LEFT:
            self.next_direction = RIGHT

    def check_food_collision(self, food):

        return self.body[0] == (food.x, food.y)

    def check_wall_collision(self):

        x, y = self.body[0]

        return (
            x < 0 or
            x >= WIN_WIDTH or
            y < 0 or
            y >= WIN_HEIGHT
        )

    def check_self_collision(self):

        return self.body[0] in self.body[1:]

    def draw(self, window):

        for segment in self.body:

            pygame.draw.rect(
                window,
                COLOR_GREEN,
                (
                    segment[0],
                    segment[1],
                    CELL_SIZE,
                    CELL_SIZE
                )
            )