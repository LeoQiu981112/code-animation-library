from pygments.lexers import get_lexer_by_name
from pygments.formatters import RawTokenFormatter
from pygments import highlight
from typing import List, Tuple
from src.nord_style import NordStyle


class CodeTokenizer:
    """
    Class for tokenizing code into a grid of characters and their types.
    """

    def __init__(self, code: str, language: str):
        """
        Initialize a new CodeTokenizer instance.

        Args:
            code: The code to tokenize.
            language: The language of the code.
        """
        self.code = code
        self.language = language
        self.grid = [[]]

    def tokenize(self) -> None:
        """
        Tokenize the code into a grid of characters and their types.
        """
        lexer = get_lexer_by_name(self.language)
        formatter = RawTokenFormatter(style=NordStyle)

        highlighted_code = highlight(self.code, lexer, formatter)

        preprocessed_tokens: str = highlighted_code.decode("utf-8").strip().split("\n")
        self.processed_tokens = []
        for token in preprocessed_tokens:
            token_type, char = token.split("\t")
            print("token_type:", token_type), print("char:", char)
            self.processed_tokens.append((token_type, char))
        print("processed token types:", self.processed_tokens, "\n")

    def populate_grid(self):
        self.tokenize()
        # populate grid by iterating over tokens
        for item in self.processed_tokens:
            token_type, str_to_eval = item
            trimmed_str = str_to_eval[1:-1]

            if str_to_eval == "'\\n'":
                # Newline: start a new line of code
                self.grid.append([])
            else:
                for char in trimmed_str:
                    # Whitespace: add to the current line
                    self.grid[-1].append((char, token_type))
