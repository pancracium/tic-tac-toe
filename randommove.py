"""New file for a method for playing random moves."""

#Import necessary modules
import random

def play(game):
        """Play a random move."""
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if game.board[x][y] == "":
                game.play(x, y)
                break