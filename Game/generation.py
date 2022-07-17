import copy
from Game.grid import Grid
from itertools import product


class Generation:
    def __init__(self):
        pass

    @staticmethod
    def _count_neighbors(x, y, grid):
        """Static helper method for finding living cells surrounding the current.

        Attributes:
            x: X coordinate
            y: Y coordinate
            grid: Grid of cells
        """
        living_neighbors = 0

        if grid.get_grid()[x][y - 1].get_state() != 0:
            living_neighbors += 1
        if grid.get_grid()[x - 1][y].get_state() != 0:
            living_neighbors += 1
        if grid.get_grid()[x - 1][y - 1].get_state() != 0:
            living_neighbors += 1
        if grid.get_grid()[x - 1][y + 1].get_state() != 0:
            living_neighbors += 1
        if grid.get_grid()[x][y + 1].get_state() != 0:
            living_neighbors += 1
        if grid.get_grid()[x + 1][y + 1].get_state() != 0:
            living_neighbors += 1
        if grid.get_grid()[x + 1][y].get_state() != 0:
            living_neighbors += 1
        if grid.get_grid()[x + 1][y - 1].get_state() != 0:
            living_neighbors += 1

        return living_neighbors

    @classmethod
    def next_generation(cls, grid):
        """Utility method for computer the next generation of cells for Conways game of life.

        Attributes:
            grid: Grid of cells
        """
        temp_grid = copy.deepcopy(grid)

        for x in range(0, grid.get_width() - 1):
            for y in range(0, grid.get_height() - 1):
                living_neighbors = cls._count_neighbors(x, y, grid)

                current_cell = grid.get_grid()[x][y].get_state()
                if current_cell == 1 and living_neighbors < 2:
                    temp_grid.get_grid()[x][y].set_state(0)
                elif current_cell == 0 and living_neighbors == 3:
                    temp_grid.get_grid()[x][y].set_state(1)
                elif current_cell == 1 and (living_neighbors == 2 or living_neighbors == 3):
                    temp_grid.get_grid()[x][y].set_state(1)
                else:
                    temp_grid.get_grid()[x][y].set_state(0)

        return temp_grid
