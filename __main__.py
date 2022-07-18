import pygame
from Game.director import Director


SIZE_CELL = 10
SIZE_WINDOW = 600


def main():
    """Driver functions for Conways game of life.

    Sets up initial game window and sends it to the director.
    """
    pygame.init()
    pygame.display.set_caption("Conways Game of Life")
    window = pygame.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))

    director = Director(window, SIZE_CELL, SIZE_WINDOW)
    director.run_game()


if __name__ == '__main__':
    main()
