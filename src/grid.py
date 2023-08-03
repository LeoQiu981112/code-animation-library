from src.tokenizer import CodeTokenizer
from src.animations import AnimationQueue
from src.character import Character
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
        self.grid = [[]]
        self.tokenizer = CodeTokenizer("python")
        self.animation_queue = AnimationQueue()

    def add_line(self):
        """
        Add a new line to the grid.
        """
        self.grid.append([])

    def get_line(self, line_number):
        """
        Get a specific line in the grid.

        Args:
            line_number: The line number of the line to get.

        Returns:
            The line at the specified line number.
        """
        return self.grid[line_number]

    def set_line(self, line_number, line):
        self.grid[line_number] = line

    def add_character(self, char, token_type, color, position):
        """
        Add a character to the current line in the grid.

        Args:
            char: The character to add.
            token_type: The token type of the character.
            color: The color of the character.
            position: The position of the character.
        """
        character = Character(char, token_type, color, position)
        self.grid[-1].append(character)

    def insert_highlighted(self, text):
        # Insert the highlighted text into the grid
        self.tokenizer.tokenize(self, text)

    # --------------------------------animation methods------------------------------------------------#

    def line(self, line_number):
        # Get a specific line in the grid
        return self.grid[line_number]

    def apply_animations(self, current_time):
        """
        Apply animations from the AnimationQueue to the grid based on the current time.

        Parameters:
            current_time (float): The current time of the video (in seconds).
        """
        for animation in self.animation_queue.animations:
            if animation.is_active(current_time):
                animation.apply(self, current_time)

    def copy(self):
        """
        Create a deep copy of this Grid.
        """
        grid_copy = Grid()
        grid_copy.grid = copy.deepcopy(self.grid)
        # The tokenizer doesn't contain any state, so we can just assign it directly
        grid_copy.tokenizer = self.tokenizer

        return grid_copy
