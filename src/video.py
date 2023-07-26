from PIL import Image, ImageDraw, ImageFont
from src.image_generator import ImageGenerator
from src.grid import Grid


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Move:
    def __init__(self, line, direction):
        self.line = line
        self.direction = direction


class FadeIn:
    def __init__(self, line):
        self.line = line


class FadeOut:
    def __init__(self, line):
        self.line = line


class GlowIn:
    def __init__(self, line):
        self.line = line


class Insert:
    def __init__(self, line, text):
        self.line = line
        self.text = text


class Inline_Insert:
    def __init__(self, line, text):
        self.line = line
        self.text = text


class Scroll:
    @classmethod
    def center_line(cls, video, line_number):
        # Calculate the scroll animation to center a specific line in the video
        pass


class Video:
    """
    Class for managing the video stream.
    """
    def __init__(self, path):
        self.path = path
        self.grid_offset = Position(0, 0)
        self.cell_width = 10
        self.cell_height = 20
        self.font_size = 15
        self.background_color = (40, 40, 40)
        self.grid = Grid()
        self.frame_generator = ImageGenerator(font_size=20, cell_width=15, cell_height=35,
                                         background_color=(40, 40, 40))

    def set_grid_offset(self, position):
        self.grid_offset = position

    def show_grid(self, grid, seconds=3):
        # Show the grid for a specific amount of time
        frame = self.frame_generator.generate_image(grid)
        frame.save("frames/frame.png")

    def show(self, grid, animations, duration):
        if not isinstance(animations, list) or not all(callable(a) for a in animations):
            raise ValueError("Animations must be a list of callable functions or methods.")
        if not isinstance(duration, int):
            raise ValueError("Duration must be an integer.")
        # Render the animations on the video frame
        for animation in animations:
            # run the animation by applying it to the grid
            # animation.apply(self.grid)
            pass
