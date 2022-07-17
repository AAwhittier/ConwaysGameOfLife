import random
from Game.cell import Cell


class Grid:
    def __init__(self, size):
        """Game grid.

        Controls the grid of cells.

        Attributes:
            _size: Height and width of the grid.
            _grid: Grid of cells.
        """
        self._size = size
        self._grid = [[Cell(random.randint(0, 1)) for i in range(size)] for j in range(size)]

    def get_grid(self):
        """Getter for _grid

            Returns:
                _grid
        """
        return self._grid

    def get_width(self):
        """Returns the width of the grid.

            Returns:
                Width of the game grid.
        """
        return len(self._grid)

    def get_height(self):
        """Getter for grid height.

            Returns:
                height of the game grid.
        """
        return len(self._grid[0])

    def get_size(self):
        """Getter for _size

            Returns:
                _size
        """
        return self._size




