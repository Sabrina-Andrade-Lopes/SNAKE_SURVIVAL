#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from const import *

from snake import Snake
from food import Food
from score import Score
from level import Level
from menu import Menu
from endscreen import EndScreen
from assets import Assets


class Game:
    """
    Classe principal responsável pelo controle do jogo.
    """

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode(
            (
                WIN_WIDTH,
                WIN_HEIGHT
            )
        )

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        self.state = MENU

        # ==========================
        # Assets (imagens e sons)
        # ==========================

        self.assets = Assets()

        self.assets.play_music()

        # ==========================
        # Telas
        # ==========================

        self.menu = Menu(
            self.window,
            self.assets
        )

        self.end_screen = EndScreen(
            self.window,
            self.assets
        )

        # ==========================
        # Objetos do jogo
        # ==========================

        self.snake = Snake()

        self.food = Food()

        self.score = Score()

        self.level = Level()

        self.food.spawn(self.snake)

    def reset_game(self):
        """
        Reinicia todos os objetos.
        """

        self.snake.reset()

        self.score.reset()

        self.level.reset()

        self.food.spawn(self.snake)

    def run(self):
        """
        Loop principal do jogo.
        """

        while self.running:

            # ==========================
            # MENU
            # ==========================

            if self.state == MENU:

                option = self.menu.run()

                if option == PLAY:

                    self.reset_game()

                    self.state = PLAY

                elif option == EXIT:

                    self.running = False

            # ==========================
            # PLAY
            # ==========================

            elif self.state == PLAY:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:

                        self.running = False

                self.snake.handle_input()

                self.update()

                self.draw()

                pygame.display.flip()

                self.clock.tick(
                    self.level.get_speed()
                )

            # ==========================
            # WIN
            # ==========================

            elif self.state == WIN:

                option = self.end_screen.run()

                if option == MENU:

                    self.state = MENU

                elif option == EXIT:

                    self.running = False

            # ==========================
            # GAME OVER
            # ==========================

            elif self.state == GAME_OVER:

                option = self.end_screen.run()

                if option == MENU:

                    self.state = MENU

                elif option == EXIT:

                    self.running = False

        pygame.quit()

    def update(self):
        """
        Atualiza todos os elementos do jogo.
        """

        self.snake.move()

        # ==========================
        # Colisão com a comida
        # ==========================

        if self.snake.check_food_collision(self.food):

            self.assets.eat_sound.play()

            self.snake.grow()

            self.score.add_point()

            self.level.update(
                self.score.get_points()
            )

            self.food.spawn(self.snake)

        # ==========================
        # Vitória
        # ==========================

        if self.check_win():

            self.end_screen.set_result(
                WIN,
                self.score.get_points()
            )

            self.state = WIN

            return

        # ==========================
        # Game Over
        # ==========================

        if self.check_game_over():

            self.assets.game_over_sound.play()

            self.end_screen.set_result(
                GAME_OVER,
                self.score.get_points()
            )

            self.state = GAME_OVER

    def draw(self):
        """
        Desenha todos os elementos na tela.
        """

        self.window.blit(
            self.assets.background_game,
            (0, 0)
        )

        self.food.draw(self.window)

        self.snake.draw(self.window)

        self.score.draw(self.window)

        self.level.draw(self.window)

    def check_win(self):
        """
        Verifica condição de vitória.
        """

        return (
            self.score.get_points()
            >= TARGET_SCORE
        )

    def check_game_over(self):
        """
        Verifica condição de derrota.
        """

        if self.snake.check_wall_collision():

            return True

        if self.snake.check_self_collision():

            return True

        return False