from pygments.lexers import get_lexer_by_name
from pygments.formatters import RawTokenFormatter
from pygments import highlight
from typing import List, Tuple


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

    def tokenize(self, grid, code) -> Tuple[List[str], List[str]]:
        """
        Tokenize the code into two lists: one for characters and one for token types.

        Returns:
            A tuple of two lists: one for characters and one for token types.
        """
        highlighted_code = highlight(code, self.lexer, self.formatter)
        preprocessed_tokens: str = highlighted_code.decode("utf-8").strip().split("\n")
        chars = []
        token_types = []
        for token in preprocessed_tokens:
            token_type, token_str = token.split("\t")
            for char in token_str[1:-1]:
                chars.append(char)
                token_types.append(token_type)

        return chars, token_types

    def populate_grid(self, grid_obj, code):
        print(grid_obj)
        chars, token_types = self.tokenize(code)
        for char, token_type in zip(chars, token_types):
            if char == "\\n":
                # Newline: start a new line of code
                grid_obj.add_line()
                print("added_line:", grid_obj.chars)
            elif char.startswith("\\u") or char.startswith("\\U"):
                char = char.encode().decode('unicode_escape')
                grid_obj.add_token(char[1:-1], "Token.Emoji")
                print("added_eomji:", grid_obj.chars)
            else:
                # Whitespace: add to the current line
                grid_obj.add_token(char, token_type)
                print("added char:", grid_obj.chars)
