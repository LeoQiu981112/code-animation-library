from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
from pilmoji import Pilmoji
from src.nord_style import NordStyle
import traceback


class ImageGenerator:
    """
    Class for generating an image of code.
    """

    def __init__(
        self,
        font_size: int = 14,
        cell_width: int = 20,
        cell_height: int = 20,
        background_color: Tuple[int, int, int] = (30, 30, 30),
    ):
        """
        Initialize a new ImageGenerator instance.

        Args:
            font_size: The font size of the characters.
            cell_width: The width of each cell in the grid.
            cell_height: The height of each cell in the grid.
            background_color: The background color of the image.
        """
        self.font_size = font_size
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.background_color = background_color

    def generate_image(self, grid_obj) -> Image:
        """
        Generate an image of the code.

        Args:
            grid: The grid of characters and their types.

        Returns:
            The generated image.
        """
        image_width = 1904
        image_height = 1088
        max_line_width = len(max(grid_obj.grid, key=len)) * self.cell_width
        max_lines = len(grid_obj.grid)
        padding_x = max((image_width - max_line_width) // 2, 0)
        padding_y = max(
            (image_height - max_lines * self.cell_height) // 2, 0
        )  # Ensure padding_y is not negative
        line_number_width = 40  # Adjust this value as needed

        # Create a new image with the specified background color
        image = Image.new(
            "RGB", (image_width, image_height), color=self.background_color
        )
        emoji_image = Pilmoji(image)
        draw = ImageDraw.Draw(image)
        font_path = "src/font/joystix.otf"
        font = ImageFont.truetype(font_path, self.font_size)
        code_style = NordStyle()
        emoji_batch = []  # Store emojis here

        try:
            for row_idx, row in enumerate(grid_obj.grid):
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
                for col_idx, char in enumerate(row):
                    x = max(
                        col_idx * self.cell_width + padding_x + line_number_width, 0
                    )  # Ensure x is not negative
                    y = max(
                        row_idx * self.cell_height + padding_y, 0
                    )  # Ensure y is not negative
                    token_type_str = grid_obj.grid_token_colors[row_idx][col_idx]
                    desired_color = code_style.get_color(token_type_str)

                    # If it's an emoji, draw differently
                    if token_type_str == "Token.Emoji":
                        emoji_batch.append((char, (x, y)))
                        emoji_image.text((x, y), char, font=font)
                    else:
                        draw.text((x, y), char, font=font, fill=desired_color)

            # Draw all emojis in a batch
            for emoji_char, emoji_pos in emoji_batch:
                emoji_image.text(emoji_pos, emoji_char, font=font)
        except Exception:
            traceback.print_exc()

        return image

    def generate_image_wrapper(args):
        # Wrapper function for generate_image, so it can handle multiple arguments
        image_generator, grid = args
        return image_generator.generate_image(grid)
