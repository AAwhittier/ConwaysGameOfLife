import pygame.sprite


class Drawable(pygame.sprite.Sprite):
    """An object which may be drawn to the screen.

    """
    def __init__(self, window):
        """Ctor for drawables.

            params:
                window - Game window to draw on
        """
        self._window = window

    def draw(self, window):
        """Draw the game object. Overriden by child classes.

        """
        pass

    def get_window(self):
        """ getter for self._window

        :return:
            _window
        """
        return self._window
