class Line:
    def __init__(self, line_number: int):
        """
        Initialize a new Line instance.

        Parameters:
            line_number: The line number of the line.
            line: The list of characters in the line.
        """
        self.line_number = line_number
        self.tokens = []

    def __repr__(self):
        output_string = ""
        for token in self.tokens:
            output_string += str(token) + ", "
        return f"Line({output_string})"

    @property
    def length(self):
        return sum(len(token.characters) for token in self.tokens)

    def add_token(self, token):
        """
        Add a new token to the line.

        Parameters:
            token: The token to add.
        """
        self.tokens.append(token)

    def get_token(self, index):
        """
        Get the token at the specified index.

        Parameters:
            index: The index of the token to get.
        """
        return self.tokens[index]

    def move(self, x, y):
        """
        Move the line by the specified amount.

        Parameters:
            x: The amount to move the line in the x direction.
            y: The amount to move the line in the y direction.
        """
        for token in self.tokens:
            token.move(x, y)

    def clear(self):
        """
        Clear the line.
        """
        self.tokens.clear()

    # allow len() to be called on a Line object
    def __len__(self):
        return len(self.tokens)

    # make it iterable over tokens
    def __iter__(self):
        return iter(self.tokens)

    # additional iterator to iterate over characters
    def iter_characters(self):
        for token in self.tokens:
            for character in token.characters:
                yield character

    def get_line_str(self):
        final_str = ""
        for token in self.tokens:
            final_str += token.get_token_str()
        return final_str

    def set_visibility(self, state: bool):
        for token in self.tokens:
            token.set_visibility(state)
