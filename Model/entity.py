#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Classe abstrata base para todas as entidades do jogo.
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = None

    @abstractmethod
    def draw(self, window):
        """
        Desenha a entidade na janela.
        """
        pass