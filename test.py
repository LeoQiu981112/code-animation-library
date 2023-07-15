from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import RawTokenFormatter
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
from pygments.styles import STYLE_MAP, get_style_by_name
from pygments.token import *
from pygments.token import Token
import webcolors

fallback_style = {
    "color": "FFFFFF",
    "default_font_style": "italic",
    "default_background_color": "#000000",
}

style = {}


def convert_color(color, source_format, target_format):
    if source_format == target_format:
        return color

    if source_format == "rgb":
        rgb_color = color
    elif source_format == "hex":
        rgb_color = webcolors.hex_to_rgb("#" + color)
    elif source_format == "name":
        rgb_color = webcolors.name_to_rgb(color)
    else:
        raise ValueError(f"Unsupported source color format: {source_format}")

    if target_format == "rgb":
        return rgb_color
    elif target_format == "hex":
        hex_color = webcolors.rgb_to_hex(rgb_color, force_long=True)
        return hex_color
    elif target_format == "name":
        color_name = webcolors.rgb_to_name(rgb_color)
        return color_name
    else:
        raise ValueError(f"Unsupported target color format: {target_format}")


class Grid:
    def __init__(
        self,
        code,
        language,
        font_size=14,
        cell_width=20,
        cell_height=20,
        background_color=(30, 30, 30),
    ):
        self.code = code
        self.language = language
        self.font_size = font_size
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.background_color = background_color
        self.grid = [[]]

    def find_font_path(self):
        fonts = [f.fname for f in font_manager.fontManager.ttflist]
        font_names = [
            "DejaVu Sans Mono",
            "Monospace",
            "Courier New",
            "Consolas",
            "FreeMono",
        ]
        for name in font_names:
            for f in fonts:
                if name.lower() in f.lower():
                    return f
        raise Exception("No suitable monospaced font found")

    def tokenize(self):
        lexer = get_lexer_by_name(self.language)
        formatter = RawTokenFormatter(style=get_style_by_name("monokai"))

        highlighted_code = highlight(self.code, lexer, formatter)
        preprocessed_tokens = highlighted_code.decode("utf-8").strip().split("\n")
        self.processed_tokens = []
        for token in preprocessed_tokens:
            # Split the token string into token type and character
            token_type, char = token.split("\t")
            self.processed_tokens.append((token_type, char))

    def populate_grid(self):
        # ... Populate the grid by iterating over tokens ...
        self.tokenize()
        # populate grid by iterating over tokens
        for item in self.processed_tokens:
            token_type, str_to_eval = item
            trimmed_str = str_to_eval[1:-1]

            # print("token_type:", token_type)
            # print("char:", char)
            if token_type == "Token.Text.Whitespace":
                self.grid.append([])
            elif str_to_eval == "' '":
                self.grid[-1].append((" ", "Token.Text.Whitespace"))
            # check trimmed_str contains space only
            else:
                for c in trimmed_str:
                    self.grid[-1].append((c, token_type))
        # print("self.grid:", self.grid)
        # print row by row
        # for row in self.grid:
        #     print(row)

    def generate_image(self):
        self.populate_grid()
        line_number_offset = 50  # Adjust this value as needed
        padding = 50  # Adjust this value as needed
        # Calculate image dimensions based on grid size
        # Set the image dimensions for YouTube
        image_width = 1280
        image_height = 1080
        max_line_width = len(max(grid.grid, key=len)) * grid.cell_width

        monokai_style = get_style_by_name("monokai")
        # Calculate the padding needed to center the code
        max_line_width = len(max(self.grid, key=len)) * self.cell_width
        padding_x = (image_width - max_line_width) // 2
        padding_y = (image_height - len(self.grid) * self.cell_height) // 2

        # # Create a new image with the specified dimensions and background color
        image = Image.new(
            "RGB", (image_width, image_height), color=self.background_color
        )
        draw = ImageDraw.Draw(image)

        # # Load the specified font
        font = ImageFont.truetype(self.find_font_path(), self.font_size)
        s = set()
        # Draw each character in the grid onto the image
        for row_idx, row in enumerate(self.grid):
            for col_idx, (char, token_type) in enumerate(row):
                x = col_idx * self.cell_width + padding_x
                y = row_idx * self.cell_height + padding_y
                if col_idx == 0:
                    # Draw the line number, but don't skip to the next iteration
                    draw.text(
                        (x - line_number_offset, y),
                        str(row_idx),
                        font=font,
                        fill=(255, 255, 255),
                    )

                token_type = Token.__getattr__(self.grid[row_idx][col_idx][1][6:])
                try:
                    token_style = monokai_style.style_for_token(token_type)
                except KeyError:
                    token_style = fallback_style
                # print("token_style:", token_style["color"])
                rgb_color = convert_color(token_style["color"], "hex", "rgb")
                # print("rgb_color:", rgb_color)
                draw.text((x, y), char, font=font, fill=rgb_color)
                # {'color': '66d9ef', 'bold': False, 'italic': False, 'underline': False, 'bgcolor': None, 'border': None, 'roman': None, 'sans': None, 'mono': None, 'ansicolor': None, 'bgansicolor': None}
        print("s:", s)
        return image


# Usage example
code = """
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
"""

language = "python"

grid = Grid(
    code,
    language,
    font_size=12,
    cell_width=15,
    cell_height=15,
    background_color=(30, 30, 30),
)
image = grid.generate_image()
image.save("hah.png")
