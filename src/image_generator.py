from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
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
        # dimensions
        image_width = 1900
        image_height = 1080
        max_line_width = len(max(self.grid, key=len)) * self.cell_width
        max_lines = len(self.grid)
        padding_x = max((image_width - max_line_width) // 2, 0)
        padding_y = max(
            (image_height - max_lines * self.cell_height) // 2, 0
        )  # Ensure padding_y is not negative
        line_number_width = 40  # Adjust this value as needed

        image = Image.new(
            "RGB", (image_width, image_height), color=self.background_color
        )
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(self.find_font_path(), self.font_size)
        code_style = NordStyle()

        # print("grid", self.grid, "\n")
        for row_idx, row in enumerate(self.grid):
            # First draw the line number
            line_number_x = max(
                padding_x - line_number_width, 0
            )  # Ensure line_number_x is not negative
            line_number_y = row_idx * self.cell_height + padding_y
            draw.text(
                (line_number_x, line_number_y),
                str(row_idx + 1),
                font=font,
                fill=(255, 255, 255),
            )

            # Then draw the code
            for col_idx, (char, token_type) in enumerate(row):
                x = max(
                    col_idx * self.cell_width + padding_x + line_number_width, 0
                )  # Ensure x is not negative
                y = max(
                    row_idx * self.cell_height + padding_y, 0
                )  # Ensure y is not negative
                token_type_str = self.grid[row_idx][col_idx][1]
                try:
                    desired_color = code_style.get_color(token_type_str)
                    draw.text((x, y), char, font=font, fill=desired_color)
                except Exception as e:
                    traceback.print_exc()
        return image
