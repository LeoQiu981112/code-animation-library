from src.image_generator import ImageGenerator
from src.grid import Grid
from src.tokenizer import CodeTokenizer
from src.video import Video


with open("src/source_code.py", "r") as file:
    # Read the file
    code_string = file.read()

if __name__ == "__main__":
    path = "clips/output_video.mp4"
    with open("src/source_code.py", "r") as file:
        # Read the file
        code_string = file.read()

    video = Video(path)
    # video.set_grid_offset(Position(10, 5))

    grid_obj = Grid()
    grid_obj.insert_highlighted(code_string)
    # image
    video.show_grid(grid_obj)

    # create video of 4 seconds
    video.show(grid_obj, 4)
    # video.show(
    #     grid,
    #     Move(grid.line(5), Direction.DOWN),
    #     Move(grid.line(6), Direction.UP),
    # )
    # video.show(grid, FadeIn(grid.line(5)), FadeOut(grid.line(6)))
    # video.show(grid, GlowIn(grid.line(5)))
    # video.show(Scroll.center_line(video, 8))
