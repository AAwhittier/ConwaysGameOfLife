# Conways Game Of Life
### Author
Aaron Whittier
 / Conways Game of Life / whi1204@byui.edu

# Overview
Conways game of life is a generational game which follows a few rules:
 1. Cells with 2 or 3 neighbors live on to the next generation.
 2. Dead cells with 3 living neighbors become alive in the following generation.
 3. All other cells die in the next generation.
 
 The game begins with a random game state. The rules of the simulation are following until it ends or becomes an infinite simulation loop.
 
 # Gameplay and Controls
 Space - pause the game
 
 Mouse click - flip a cell between dead and alive states. This may be done while the simulation is running, or while it is paused to change multiple cells before the next generation begins.

# Dependencies
Pygame
Install: python3 -m pip install pygame
https://www.pygame.org/
