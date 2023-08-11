class Character:
    def __init__(self, char, position, color):
        self.char = char
        self.position = position
        self.color = color
        self.visible = False

    def __repr__(self):
        return f"char:{self.char}, pos:({self.position.x}, {self.position.y}),color:{self.color}, visible:{self.visible}"

    def move(self, x, y):
        self.position.x += x
        self.position.y += y

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def set_visibility(self, state: bool):
        self.visible = state

    def is_visible(self):
        return self.visible
