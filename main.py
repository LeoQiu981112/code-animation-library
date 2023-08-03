import os
import time
from src.video import Video
from src.grid import Grid
from src.animations import FadeIn, FadeOut, TypingEffect

if __name__ == "__main__":
    os.system("rm frames/*")
    video_path = "clips/output_video.mp4"

    # Read the code from a file
    with open("src/source_code.py", "r") as file:
        code_string = file.read()

    # Initialize a grid and insert the code
    grid = Grid()
    grid.insert_highlighted(code_string)

    # FADE IN first 3 lines
    grid.animation_queue.add_animation(FadeIn(0, 1, 0))
    grid.animation_queue.add_animation(FadeIn(0, 1, 1))
    grid.animation_queue.add_animation(FadeIn(0, 1, 2))

    # FADE OUT lines 6-8
    grid.animation_queue.add_animation(FadeOut(0, 4, 5))
    grid.animation_queue.add_animation(FadeOut(0, 4, 6))
    grid.animation_queue.add_animation(FadeOut(0, 4, 7))

    # type lines 11-13
    grid.animation_queue.add_animation(TypingEffect(1, 1.5, 10))
    grid.animation_queue.add_animation(TypingEffect(2, 2.5, 11))
    grid.animation_queue.add_animation(TypingEffect(3, 3.5, 12))

    # Create a Video object
    video = Video(video_path)

    # Record the start time
    start_time = time.time()

    # Render the video
    video.render_video(grid, duration=8, fps=10)

    # Calculate and print the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Video rendering took {elapsed_time} seconds")

    # Delete all files in frames folder
    # os.system("rm frames/*")
