from src.grid import Grid
from src.video import Video
from src.animation import FadeIn
import time


with open("src/source_code.py", "r") as file:
    # Read the file
    code_string = file.read()

if __name__ == "__main__":
    video_path = "clips/output_video.mp4"
    with open("src/source_code.py", "r") as file:
        # Read the file
        code_string = file.read()

    video = Video(video_path)
    # video.set_grid_offset(Position(10, 5))

    grid_obj = Grid()
    grid_obj.insert_highlighted(code_string)
    # create video of 4 seconds
    start_time = time.time()
    # Create a FadeInAnimation that will start at time 2 seconds and last for 1 second,
    # targeting the line number 2 (assuming line numbering starts from 0)
    fade_in_animation = FadeIn(2.0, 1.0, 2)

    # Add the animation to the animation queue in the grid
    grid_obj.animation_queue.add_animation(fade_in_animation)

    # Now, you can call `apply_animations` at the appropriate time to apply the animations
    # to the grid. For example, if your current time is 2.5 seconds, you can do:
    current_time = 2.5
    grid_obj.apply_animations(current_time)
    video.render_video(grid_obj, 5)

    # The line number 2 in the grid will now be faded in based on the time 2.5 seconds.
    end_time = time.time()

    print(f'Video creation took {end_time - start_time} seconds')

    # video.show(
    #     grid,
    #     Move(grid.line(5), Direction.DOWN),
    #     Move(grid.line(6), Direction.UP),
    # )
    # video.show(grid, FadeIn(grid.line(5)), FadeOut(grid.line(6)))
    # video.show(grid, GlowIn(grid.line(5)))
    # video.show(Scroll.center_line(video, 8))
