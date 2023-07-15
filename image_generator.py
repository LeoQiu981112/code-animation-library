from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
from pygments.token import Token
from color_converter import ColorConverter
from nord_style import NordStyle
import traceback


class ImageGenerator:
    """
    Class for generating an image of code.
    """

    def __init__(
        self,
        grid: List[List[Tuple[str, str]]],
        font_size: int = 14,
        cell_width: int = 20,
        cell_height: int = 20,
        background_color: Tuple[int, int, int] = (30, 30, 30),
    ):
        """
        Initialize a new ImageGenerator instance.

        Args:
            grid: The grid of characters and their types.
            font_size: The font size of the characters.
            cell_width: The width of each cell in the grid.
            cell_height: The height of each cell in the grid.
            background_color: The background color of the image.
        """
        self.grid = grid
        self.font_size = font_size
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.background_color = background_color

    @staticmethod
    def find_font_path() -> str:
        """
        Find the path to a suitable monospaced font.

        Returns:
            The path to a suitable monospaced font.

        Raises:
            Exception: If no suitable monospaced font is found.
        """
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

    def generate_image(self) -> Image:
        """
        Generate an image of the code.

        Returns:
            The generated image.
        """
        image_width = 1900
        image_height = 1080

        max_line_width = len(max(self.grid, key=len)) * self.cell_width
        padding_x = (image_width - max_line_width) // 2
        padding_y = (image_height - len(self.grid) * self.cell_height) // 2
        line_number_offset = 50  # Adjust this value as needed

        image = Image.new(
            "RGB", (image_width, image_height), color=self.background_color
        )
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(self.find_font_path(), self.font_size)
        code_style = NordStyle()
        tokens_set = set()
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
                token_type_str = self.grid[row_idx][col_idx][1].replace("Token.", "")

                token_type = getattr(Token, token_type_str)
                if token_type not in tokens_set:
                    tokens_set.add(token_type)
                try:
                    desired_color = code_style.get_color(token_type)
                    rgb_color = ColorConverter.convert_color(
                        desired_color, "hex", "rgb"
                    )
                    draw.text((x, y), char, font=font, fill=rgb_color)
                except Exception as e:
                    # traceback.print_exc()
                    # end program
                    pass
        return image
