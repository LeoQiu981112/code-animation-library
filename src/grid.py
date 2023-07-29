from src.tokenizer import CodeTokenizer
from src.animation import AnimationQueue
from typing import List, Tuple
import copy


class Grid:
    """
    Class for managing the grid of characters and their types.
    """
# -------------------------------initialize-------------------------------------------------#

    def __init__(self):
        """
        Initialize a new CodeGrid instance.
        """
        self.token_strs = []
        self.token_types = []
        self.grid = [[]]
        self.grid_token_colors = [[]]
        self.tokenizer = CodeTokenizer("python")
        self.animation_queue = AnimationQueue()

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

    def insert_highlighted(self, text):
        # Insert the highlighted text into the grid
        self.tokenizer.populate_grid(self, text)

# --------------------------------animation methods------------------------------------------------#

    def line(self, line_number):
        # Get a specific line in the grid
        return self.strs[line_number], self.token_types[line_number]

    def get_line_colors(self, line_number: int) -> List[Tuple[int, int, int]]:
        return self.grid_token_colors[line_number]

    def apply_animations(self, current_time):
        """
        Apply animations from the AnimationQueue to the grid based on the current time.

        Parameters:
            current_time (float): The current time of the video (in seconds).
        """
        for animation in self.animation_queue.animations:
            if animation.is_active(current_time):
                self.grid = animation.apply(self.grid, current_time)

    def copy(self):
        """
        Create a deep copy of this Grid.
        """
        grid_copy = Grid()
        grid_copy.token_strs = copy.deepcopy(self.token_strs)
        grid_copy.token_types = copy.deepcopy(self.token_types)
        grid_copy.grid = copy.deepcopy(self.grid)
        grid_copy.grid_token_colors = copy.deepcopy(self.grid_token_colors)
        # The tokenizer doesn't contain any state, so we can just assign it directly
        grid_copy.tokenizer = self.tokenizer

        return grid_copy
