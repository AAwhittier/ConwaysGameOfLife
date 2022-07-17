import pygame


class Button:
    def __init__(self, window, x, y, width, height, text=""):
        self._window = window
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._test = text

    def draw_button(self):
        pygame.draw.rect(self._window, (211, 211, 211), (self._x, self._y, self._width, self._height), 0)

