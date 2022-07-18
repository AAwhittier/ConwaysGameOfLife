class InputHandle:
    """Interprets input from the user into meaningful game data.

    """
    def __init__(self):
        pass

    @classmethod
    def parse_click(cls, pos, scale):
        """Interpret a game input click based on its pixel position and the scale of the game.

        Properties:
            @classmethod

         Args:
             pos - Position in pixels of the cursor click.
             scale - The relative scale of the game.
         """
        # Floor division to get a whole number for the location in the game.
        row = pos[0] // scale
        col = pos[1] // scale

        return row, col
