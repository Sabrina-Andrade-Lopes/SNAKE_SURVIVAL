#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity


class Snake(Entity):
    def __init__(self):
        self.body = None
        self.direction = None
        self.speed = None

    def move(self, ):
        pass

    def grow(self, ):
        pass

    def change_direction(self, dir):
        pass

    def check_self_collision(self, ):
        pass

    def draw(self, window):
        pass
