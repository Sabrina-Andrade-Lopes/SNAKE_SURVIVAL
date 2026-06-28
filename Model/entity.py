#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Entity(ABC):

    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, window):
        pass