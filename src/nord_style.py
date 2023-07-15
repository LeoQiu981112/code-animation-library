# create custom token Token.Text.Whitespace


class NordStyle:
    styles = {
        "Token.Comment": "#81a1c1",  # Comment style (light blue)
        "Token.Comment.Single": "#81a1c1",  # Single Comment style (light blue)
        "Token.Keyword": "#b48ead",  # Keyword style (light purple)
        "Token.Keyword.Constant": "#b48ead",  # Constant Keyword style (light purple)
        "Token.Name": "#88c0d0",  # Name style (light blue)
        "Token.String": "#a3be8c",  # String style (light green)
        "Token.Error": "#bf616a",  # Error style (light red)
        "Token.Number": "#8fbcbb",  # Number style (light teal)
        "Token.Literal.String.Double": "#a3be8c",  # String style (light green)
        "Token.Literal.String.Escape": "#ebcb8b",  # String Escape style (light yellow)
        "Token.Literal.Number.Integer": "#8fbcbb",  # Integer style (light teal)
        "Token.Operator": "#81a1c1",  # Operator style (light blue)
        "Token.Punctuation": "#81a1c1",  # Punctuation style (light blue)
        "Token.Literal.String.Doc": "#81a1c1",  # String Doc style (light blue)
        "Token.Text": "#8fbcbb",  # Text style (light teal)
        "Token.Text.Whitespace": "#d8dee9",  # Whitespace style (silver/gray)
        "Token.Keyword.Namespace": "#b48ead",  # Keyword Namespace style (light purple)
        "Token.Name.Class": "#bf616a",  # Class Name style (light red)
        "Token.Name.Namespace": "#81a1c1",  # Namespace Name style (light blue)
        "Token.Name.Function": "#bf616a",  # Function Name style (light red)
        "Token.Name.Function.Magic": "#bf616a",  # Magic Function Name style (light red)
        "Token.Name.Builtin.Pseudo": "#bf616a",  # Builtin Pseudo Name style (light red)
        "Token.Operator.Word": "#81a1c1",  # Operator Word style (light blue)
        "Token.Name.Builtin": "#bf616a",  # Builtin Name style (light red)
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
