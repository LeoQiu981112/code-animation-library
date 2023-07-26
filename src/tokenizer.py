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

    def tokenize(self, code) -> List[Tuple[str, str]]:
        """
        Tokenize the code into a list of tuples containing token type and character.

        Returns:
            A list of tuples containing token type and character.
        """
        highlighted_code = highlight(code, self.lexer, self.formatter)
        preprocessed_tokens: str = highlighted_code.decode("utf-8").strip().split("\n")

        processed_tokens = []
        for token in preprocessed_tokens:
            token_type, token_str = token.split("\t")
            processed_tokens.append((token_type, token_str[1:-1]))

        return processed_tokens

    def populate_grid(self, grid_obj, code):
        processed_tokens = self.tokenize(code)
        for token_type, str_to_eval in processed_tokens:
            if str_to_eval == "\\n":
                # Newline: start a new line of code
                grid_obj.add_line()
            elif str_to_eval.startswith("\\u") or str_to_eval.startswith("\\U"):
                str_to_eval = str_to_eval.encode().decode('unicode_escape')
                grid_obj.add_token(str_to_eval[1:-1], "Token.Emoji")
            else:
                for char in str_to_eval:
                    # Whitespace: add to the current line
                    grid_obj.add_token(char, token_type)
