from pygments.lexers import get_lexer_by_name
from pygments.formatters import RawTokenFormatter
from pygments import highlight
from typing import List, Tuple
from src.position import Position
from src.nord_style import NordStyle
from src.custom_token import Token
from src.character import Character
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.grid import Grid

NEWLINE = "\\n"


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

    def process_token(
        self, token: str, counter: int, line_number: int
    ) -> Tuple[Token, int]:
        """
        Process an individual token and return the resulting Token object and updated counter.
        """
        token_type, token_str = token.split("\t")
        color = self.code_style.get_color(token_type)
        token_obj = Token(token_type, color)
        token_str = token_str[1:-1]  # Remove the surrounding quotes

        for _, char in enumerate(token_str):
            position = Position(
                counter, line_number
            )  # Use line_number for y-coordinate
            character_obj = Character(char, position, color)
            token_obj.add_character(character_obj)
            counter += 1

        return token_obj, counter

    def tokenize_line(self, line_obj: "Line", code: str) -> None:
        line_obj.clear()  # Clear the existing tokens
        preprocessed_tokens: str = (
            highlight(code, get_lexer_by_name(self.language), self.formatter)
            .decode("utf-8")
            .strip()
            .split("\n")
        )
        counter = 0

        for token in preprocessed_tokens:
            if token.split("\t")[1][1:-1] == NEWLINE:  # If token represents a newline
                continue
            token_obj, counter = self.process_token(
                token, counter, line_obj.line_number
            )
            line_obj.add_token(token_obj)

    def tokenize_grid(self, grid_obj: "Grid", code: str) -> None:
        lines = code.split("\n")
        for line_number, line in enumerate(lines):
            line_obj = grid_obj.get_line(line_number)
            self.tokenize_line(line_obj, line)
