from src.tokenizer import CodeTokenizer


class Grid:
    """
    Class for managing the grid of characters and their types.
    """

    def __init__(self):
        """
        Initialize a new CodeGrid instance.
        """
        self.token_strs = []
        self.token_types = []
        self.grid = [[]]
        self.grid_token_colors = [[]]

        self.tokenizer = CodeTokenizer("python")

    def add_line(self):
        """
        Add a new line to the grid.
        """
        self.grid.append([])
        self.grid_token_colors.append([])

    def add_token(self, char, token_type):
        """
        Add a character and its token type to the current line in the grid.

        Args:
            char: The character to add.
            token_type: The token type of the character.
        """
        self.grid[-1].append(char)
        self.grid_token_colors[-1].append(token_type)

    def get_line(self, line_number):
        # Get a specific line in the grid
        return self.strs[line_number], self.token_types[line_number]

    def insert_highlighted(self, text):
        # Insert the highlighted text into the grid
        self.tokenizer.populate_grid(self, text)
