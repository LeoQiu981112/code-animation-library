from typing import Tuple
from PIL import Image, ImageDraw, ImageFont


class ImageGenerator:
    """
    Class for generating an image of code.
    """

    IMAGE_WIDTH = 1920
    IMAGE_HEIGHT = 1088
    LINE_NUMBER_X = 30

    def __init__(
        self,
        font_size: int = 30,
        cell_width: int = 30,
        cell_height: int = 30,
        background_color: Tuple[int, int, int, int] = (40, 40, 40, 255),
        show_line_numbers: bool = False,
        line_number_width: int = 20,
    ):
        """
        Initialize a new ImageGenerator instance.
        """
        self.font_size = font_size
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.background_color = background_color
        self.show_line_numbers = show_line_numbers
        self.line_number_width = line_number_width
        self.font = ImageFont.truetype("src/font/mono.ttf", self.font_size)
        self.padding_x = 50
        self.padding_y = 10

    def grid_to_image_coordinates(self, x: int, y: int) -> Tuple[int, int]:
        """
        Convert grid coordinates to image coordinates.
        """
        image_x = x * self.cell_width + self.padding_x + self.line_number_width
        image_y = y * self.cell_height + self.padding_y
        return image_x, image_y

    def draw_line_number(self, draw, line_idx: int):
        line_number_y = line_idx * self.cell_height + self.padding_y
        draw.text(
            (self.LINE_NUMBER_X, line_number_y),
            str(line_idx + 1),
            font=self.font,
            fill=(255, 255, 255, 255),
        )

    def draw_character(self, draw, character):
        if character.is_visible():
            x, y = self.grid_to_image_coordinates(
                character.position.x, character.position.y
            )
            draw.text((x, y), character.char, font=self.font, fill=character.color)

    def generate_image(self, grid_obj) -> Image:
        image = Image.new(
            "RGBA", (self.IMAGE_WIDTH, self.IMAGE_HEIGHT), color=self.background_color
        )
        draw = ImageDraw.Draw(image)

        for line_idx, line in enumerate(grid_obj.grid):
            if self.show_line_numbers:
                self.draw_line_number(draw, line_idx)

            for token in line:
                for character in token.characters:
                    self.draw_character(draw, character)

        return image
