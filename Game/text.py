from Game.drawable import Drawable
import pygame


class Text(Drawable):
    def __init__(self):
        super.__init__()

    def draw(self, window):
        """ Draw the text to the screen.

        :param window:
        :return: none
        """
        window.blit(self.get_text(), (self.get_x(), self.get_y()))
