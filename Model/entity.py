#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Classe abstrata que representa uma entidade do jogo.

    Todas as entidades possuem uma posição (x, y) e devem
    implementar o método draw().
    """

    def __init__(self, x=0, y=0):
        """
        Inicializa a entidade.

        Args:
            x (int): posição horizontal.
            y (int): posição vertical.
        """

        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, window):
        """
        Desenha a entidade na janela.

        Args:
            window: superfície do pygame onde a entidade será desenhada.
        """
        pass