from pygments.style import Style
from pygments.token import (
    Comment,
    Keyword,
    Name,
    String,
    Error,
    Number,
    Operator,
    Punctuation,
)


class NordStyle(Style):
    default_style = "#81a1c1"
    styles = {
        Comment: "#81a1c1",  # Comment style
        Keyword: "#81a1c1",  # Keyword style
        Name: "#81a1c1",  # Name style
        String: "#a3be8c",  # String style
        Error: "#bf616a",  # Error style
        Number: "#b48ead",  # Number style
        Operator: "#81a1c1",  # Operator style
        Punctuation: "#81a1c1",  # Punctuation style
    }

    def get_color(self, token_type):
        color = self.styles.get(token_type)
        if color:
            return color
        else:
            print("No color found for token type:", token_type)
            return "#81a1c1"


# highlighted_code = highlight(code, lexer, formatter)
# print(highlighted_code)
