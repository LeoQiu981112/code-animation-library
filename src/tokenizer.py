from pygments.lexers import get_lexer_by_name
from pygments.formatters import RawTokenFormatter
from pygments import highlight
from typing import List, Tuple
from src.character import Character
from src.position import Position
from src.nord_style import NordStyle


class CodeTokenizer:
    """
    Class for tokenizing code into a grid of characters and their types.
    """

    def __init__(self, language: str):
        """
        Initialize a new CodeTokenizer instance.

        Args:
            code: The code to tokenize.
            language: The language of the code.
        """
        self.language = language
        self.lexer = get_lexer_by_name(self.language)
        self.formatter = RawTokenFormatter()
        self.code_style = NordStyle()

    def tokenize(self, grid_obj, code):
        """
        Tokenize the code into two lists: one for characters and one for token types.
        """
        highlighted_code = highlight(code, self.lexer, self.formatter)
        preprocessed_tokens: str = highlighted_code.decode("utf-8").strip().split("\n")

        counter = 0
        for token in preprocessed_tokens:
            token_type, token_str = token.split("\t")
            token_str = token_str[1:-1]  # Remove the surrounding quotes
            if token_str == "\\n":
                # Newline: start a new line of code
                grid_obj.add_line()
                counter = 0  # Reset the counter for each new line
                continue  # Skip to the next token
            elif token_str.startswith("\\u") or token_str.startswith("\\U"):
                token_str = token_str.encode().decode("unicode_escape")
                token_type = "Token.Emoji"
            color = self.code_style.get_color(token_type)
            for i, char in enumerate(token_str):
                # Create a new Character object for each character
                position = Position(counter, len(grid_obj.grid) - 1)
                grid_obj.add_character(char, token_type, color, position)
                counter += 1  # Increase the counter for each character
