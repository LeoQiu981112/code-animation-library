from pygments.lexers import get_lexer_by_name
from pygments.formatters import RawTokenFormatter
from pygments import highlight
from typing import List, Tuple
from nord_style import NordStyle


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
        s = set()

        highlighted_code = highlight(self.code, lexer, formatter)
        preprocessed_tokens: str = highlighted_code.decode("utf-8").strip().split("\n")
        self.processed_tokens = []
        for token in preprocessed_tokens:
            token_type, char = token.split("\t")
            self.processed_tokens.append((token_type, char))
            if token_type not in s:
                s.add(token_type)
        print("processed token types:", s, "\n")

    def populate_grid(self):
        # ... Populate the grid by iterating over tokens ...
        self.tokenize()
        # populate grid by iterating over tokens
        for item in self.processed_tokens:
            token_type, str_to_eval = item
            trimmed_str = str_to_eval[1:-1]
            if token_type == "Token.Text.Whitespace":
                self.grid.append([])
                self.grid[-1].append(("", "Token.Text.Whitespace"))
            elif str_to_eval == "' '":
                self.grid[-1].append((" ", "Token.Text.Whitespace"))
            # check trimmed_str contains space only
            else:
                for c in trimmed_str:
                    # WE CAN ASSIGN COLOR INSTEAD OF TOKEN TYPE RIGHT HERE
                    # DO THE EVAL RIGHT NOW
                    self.grid[-1].append((c, token_type))

    def get_grid(self) -> List[List[Tuple[str, str]]]:
        """
        Get the grid of characters and their types.

        Returns:
            The grid of characters and their types.
        """
        return self.grid
