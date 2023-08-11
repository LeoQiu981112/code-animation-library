from src.tokenizer import CodeTokenizer
from src.line import Line
from typing import List
import copy


class Grid:
    """
    Class for managing the grid of characters and their types.
    """

    def __init__(self: "Grid"):
        """
        Initialize a new CodeGrid instance.

        Parameters:
            lines_in_use (int): The number of lines in use.
            grid (List[Line]): The grid of characters and their types.
            tokenizer (CodeTokenizer): The tokenizer used to tokenize the grid.
        """
        self.lines_in_use = 0
        self.grid: List[Line] = [Line(i) for i in range(50)]
        self.tokenizer: CodeTokenizer = CodeTokenizer("python")

    def get_line(self: "Grid", line_number: int) -> Line:
        """
        Get a specific line in the grid.
        """
        return self.grid[line_number]

    def set_line(self: "Grid", line_number: int, line: Line) -> None:
        """
        Set a specific line in the grid.
        """
        self.grid[line_number] = line

    def insert_highlighted(self: "Grid", text: str) -> None:
        """
        Insert highlighted code into the grid.
        """
        self.tokenizer.tokenize_grid(self, text)

    def copy(self) -> "Grid":
        """
        Create a deep copy of this Grid.
        """
        grid_copy = Grid()
        grid_copy.grid = copy.deepcopy(self.grid)
        return grid_copy
