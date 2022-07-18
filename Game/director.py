from Game.grid import Grid
from Game.generation import Generation
from Game.inputhandle import InputHandle
from Game.text import Text
import pygame


class Director:
    """Game director.=.

    Controls the behaviour of the game.

    Attributes:

    """

    COLOR_ALIVE = (220, 20, 60)
    COLOR_DEAD = (220, 220, 220)
    OFFSET = 2

    def __init__(self, window, size_cell, size_window):
        """Constructs a new Director.

         Controls the flow of play for the Hilo game.

         Args:
             self (Director): an instance of Deck.
             window: Game frame
             size_cell: building block of the window
             size_window: Size of the game display screen.
         """
        self._window = window
        self._running = True
        self._field_active = False
        self._grid = Grid(int(size_window / size_cell))
        self._size_cell = size_cell
        self._buttons = []

    def run_game(self):
        """Start the core game loop.

         Args:
             self (Director): An instance of Director.
         """

        while self._running:

            # Handle pygame events.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._field_active = not self._field_active

                # Interpret input clicks and locate them.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_pos = event.pos
                    m_pos = InputHandle.parse_click(m_pos, self._size_cell + self.OFFSET)

                    self._grid.get_grid()[m_pos[0]][m_pos[1]].invert_cell()

                # Terminate game.
                if event.type == pygame.QUIT:
                    self._running = False

            self._update()
            pygame.display.update()

    def _update(self):
        """Walk through the games elements and change them as needed.

         Args:
         """
        for x in range(self._grid.get_width()):
            for y in range(self._grid.get_height()):
                cell = pygame.Rect(x * (self._size_cell + self.OFFSET), y * (self._size_cell + self.OFFSET),
                                   self._size_cell, self._size_cell)

                if self._grid.get_grid()[x][y].get_state() == 1:
                    pygame.draw.rect(self._window, self.COLOR_ALIVE, cell)
                else:
                    pygame.draw.rect(self._window, self.COLOR_DEAD, cell)

        if not self._field_active:
            self._grid = Generation.next_generation(self._grid)
