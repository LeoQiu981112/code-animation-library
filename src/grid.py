from typing import List, Tuple
from src.tokenizer import CodeTokenizer


class Grid:
    """
    Class for managing the grid of characters and their types.
    """

    def __init__(self):
        """
        Initialize a new CodeGrid instance.
        """
        self.lines = [[]]
        self.tokenizer = CodeTokenizer("python")

    def add_line(self):
        """
        Add a new line to the grid.
        """
        self.lines.append([])

    def add_token(self, char, token_type):
        """
        Add a character and its token type to the current line in the grid.

        Args:
            char: The character to add.
            token_type: The token type of the character.
        """
        self.lines[-1].append((char, token_type))

    def get_grid(self) -> List[List[Tuple[str, str]]]:
        """
        Get the grid of characters and their types.

        Returns:
            The grid of characters and their types.
        """
        return self.lines

    def get_line(self, line_number):
        # Get a specific line in the grid
        return self.lines[line_number]

    def insert_highlighted(self, text):
        # Insert the highlighted text into the grid
        self.tokenizer.populate_grid(self, text)
