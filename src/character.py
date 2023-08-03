class Character:
    def __init__(self, char, token_type, color, position):
        self.char = char
        self.token_type = token_type
        self.color = color
        self.position = position

    def __repr__(self):
        return f"Character({self.char}, {self.position.x}, {self.position.y})"
