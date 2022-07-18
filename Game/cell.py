class Cell:
    def __init__(self, state):
        """A single cell within the grid.

        Controls whether a cell is alive or dead in the game.

        Attributes:
            _state: 1- Alive 0- Dead
        """
        self._state = state

    def invert_cell(self):
        """Sets a cell state to its inverse value.

        """
        self._state = not self._state

    def get_state(self):
        """Getter for _state

            Returns:
                _state
        """
        return self._state

    def set_state(self, state):
        """Setter for _state

        """
        self._state = state
