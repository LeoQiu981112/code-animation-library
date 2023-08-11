from src.position import Position


class Token:
    def __init__(self, token_type, color):
        self.characters = []
        self.token_type = token_type
        self.color = color

    def __repr__(self):
        return f"Token({self.token_type}, {self.characters})"

    def get_token_str(self):
        final_string = ""
        for character in self.characters:
            final_string += character.char
        return final_string

    def add_character(self, character):
        self.characters.append(character)

    def get_character(self, index):
        return self.characters[index]

    def get_character_position(self, char_index: int) -> Position:
        return Position(self.start_position.x + char_index, self.start_position.y)

    def move(self, x, y):
        for character in self.characters:
            character.move(x, y)

    def get_color(self):
        return self.color

    def set_color(self, color):
        for character in self.characters:
            character.set_color(color)

    def set_visibility(self, state: bool):
        for character in self.characters:
            character.set_visibility(state)
