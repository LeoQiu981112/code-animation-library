import numpy as np
from src.tokenizer import CodeTokenizer

class Grid:
    """
    Class for managing the grid of characters and their types.
    """

    def __init__(self):
        """
        Initialize a new CodeGrid instance.
        """
        self.chars = np.array([[]], dtype=str)
        self.token_types = np.array([[]], dtype=str)
        self.tokenizer = CodeTokenizer("python")

    def add_line(self):
        """
        Add a new line to the grid.
        """
        self.chars = np.vstack([self.chars, []])
        self.token_types = np.vstack([self.token_types, []])
        print("add line:", self.chars)

    def add_token(self, char, token_type):
        """
        Add a character and its token type to the current line in the grid.

        Args:
            char: The character to add.
            token_type: The token type of the character.
        """
        self.chars[-1] = np.append(self.chars[-1], char)
        self.token_types[-1] = np.append(self.token_types[-1], token_type)

    def get_grids(self):
        """
        Get the grid of characters and their types.

        Returns:
            The grid of characters and their types.
        """
        return self.chars, self.token_types

    def get_line(self, line_number):
        # Get a specific line in the grid
        return self.chars[line_number], self.token_types[line_number]

    def insert_highlighted(self, text):
        # Insert the highlighted text into the grid
        self.tokenizer.populate_grid(self, text)
        print(self.chars)
