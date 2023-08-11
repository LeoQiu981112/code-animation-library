class NordStyle:
    styles = {
        "Token.Comment": "#81a1c1",  # Comment style (light blue)
        "Token.Comment.Single": "#81a1c1",  # Single Comment style (light blue)
        "Token.Keyword": "#b48ead",  # Keyword style (light purple)
        "Token.Keyword.Constant": "#b48ead",  # Constant Keyword style (light purple)
        "Token.Name": "#88c0d0",  # Name style (light blue)
        "Token.String": "#a3be8c",  # String style (light green)
        "Token.Literal.String.Single": "#a3be8c",  # String Single style (light green)
        "Token.Error": "#8f99a3",  # Error style (cool red)
        "Token.Number": "#8fbcbb",  # Number style (light teal)
        "Token.Literal.String.Double": "#a3be8c",  # String style (light green)
        "Token.Literal.String.Escape": "#ebcb8b",  # String Escape style (light yellow)
        "Token.Literal.Number.Integer": "#8fbcbb",  # Integer style (light teal)
        "Token.Literal.Number.Float": "#8fbcbb",  # Float style (light teal)
        "Token.Operator": "#81a1c1",  # Operator style (light blue)
        "Token.Punctuation": "#81a1c1",  # Punctuation style (light blue)
        "Token.Literal.String.Doc": "#81a1c1",  # String Doc style (light blue)
        "Token.Text": "#8fbcbb",  # Text style (light teal)
        "Token.Text.Whitespace": "#d8dee9",  # Whitespace style (silver/gray)
        "Token.Keyword.Namespace": "#b48ead",  # Keyword Namespace style (light purple)
        # Adjusted red colors for better aesthetics and readability
        "Token.Name.Class": "#c76f7f",  # Class Name style (adjusted red)
        "Token.Name.Namespace": "#81a1c1",  # Namespace Name style (light blue)
        "Token.Name.Function": "#c76f7f",  # Function Name style (adjusted red)
        "Token.Name.Function.Magic": "#c76f7f",  # Magic Function Name style (adjusted red)
        "Token.Name.Builtin.Pseudo": "#c76f7f",  # Builtin Pseudo Name style (adjusted red)
        "Token.Name.Exception": "#c76f7f",  # Exception Name style (adjusted red)
        "Token.Operator.Word": "#81a1c1",  # Operator Word style (light blue)
        "Token.Name.Builtin": "#c76f7f",  # Builtin Name style (adjusted red)
    }

    def get_color(self, token_type):
        color_hex = self.styles.get(token_type)
        if color_hex:
            # Convert the hexadecimal color to an RGB tuple
            color_rgb = tuple(int(color_hex[i : i + 2], 16) for i in (1, 3, 5))
            return color_rgb + (255,)  # Added alpha value
        else:
            print("No color found for token type:", token_type)
            return (130, 177, 255, 255)  # Default color with alpha value
