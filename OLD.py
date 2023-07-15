from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager

# Tomorrow Night theme colors
BACKGROUND_COLOR = (29, 31, 33)  # Very dark color for the background
LINE_NUMBER_COLOR = (147, 161, 161)  # Lighter color for line numbers
TEXT_COLOR = (248, 248, 242)  # Off-white color for the text

class Grid:
    def __init__(self, code, language, font_name='arial', dpi=300, image_width=1280, image_height=720, cell_width=10, cell_height=20):
        self.code = code
        self.language = language
        self.font_name = font_name
        self.dpi = dpi
        self.font_path = self.find_font_path(font_name)
        self.image_width = image_width
        self.image_height = image_height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.grid = []

    def find_font_path(self, font_name):
        fonts = [f.fname for f in font_manager.fontManager.ttflist]
        for f in fonts:
            if font_name.lower() in f.lower():
                return f
        raise Exception(f"Font '{font_name}' not found")

    def tokenize(self):
        lexer = get_lexer_by_name(self.language)
        tokens = list(lexer.get_tokens(self.code))
        line = []
        for token_type, token_value in tokens:
            if token_value == "\n":
                self.grid.append(line)
                line = []
            else:
                line.extend(list(token_value))
        if line:
            self.grid.append(line)

    def generate_image(self):
        self.tokenize()

        max_line_number = len(self.grid)
        max_line_number_width = len(str(max_line_number))
        line_number_padding = self.cell_width * (max_line_number_width + 2)  # Adding more space

        code_width = max(len(max(self.grid, key=len)) * self.cell_width, self.image_width - line_number_padding)
        code_height = len(self.grid) * self.cell_height

        font_size = int(min(self.cell_width, self.cell_height * self.image_height // code_height) * 1.3)  # Increase font size by 30%
        font = ImageFont.truetype(self.font_path, font_size)

        image = Image.new('RGB', (self.image_width * self.dpi, self.image_height * self.dpi), color=BACKGROUND_COLOR)
        draw = ImageDraw.Draw(image)

        # Draw line numbers
        for i in range(max_line_number):
            x = self.cell_width * (max_line_number_width - len(str(i + 1))) * self.dpi
            y = i * self.cell_height * self.dpi
            draw.text((x, y), str(i + 1), font=font, fill=LINE_NUMBER_COLOR)

        # Draw code characters
        for row_idx, row in enumerate(self.grid):
            for col_idx, char in enumerate(row):
                x = (line_number_padding + col_idx * self.cell_width) * self.dpi
                y = row_idx * self.cell_height * self.dpi
                draw.text((x, y), char, font=font, fill=TEXT_COLOR)

        return image.resize((self.image_width, self.image_height), Image.ANTIALIAS)

# Usage example
code = """
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
"""

language = "python"

grid = Grid(code, language, font_name='arial', dpi=300, image_width=1280, image_height=720, cell_width=10, cell_height=20)
image = grid.generate_image()
image.show()