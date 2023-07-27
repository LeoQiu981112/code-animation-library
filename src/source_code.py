from pygments.lexers import get_lexer_by_name
from pygments.formatters import RawTokenFormatter
from pygments import highlight
from typing import List, Tuple
from src.nord_style import NordStyle
import tokenize as tk
from io import BytesIO
import ast

class CodeTokenizer:
    """
    Class for tokenizing code into a grid of characters and their types.
    """

    def __init__(self, code: str, language: str):
        self.code = code
        self.language = language
        self.grid = [[]]
