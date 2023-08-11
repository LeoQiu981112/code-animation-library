import os
import time
from src.grid import Grid
from src.video import Video
from src.animations import (
    FadeIn,
    WipeLine,
    TypingEffect,
    ScrollToLine,
    UpdateLineContent,
)
from src.image_generator import ImageGenerator
from multiprocessing import Pool, freeze_support

frame_generator = ImageGenerator(
    font_size=60,  # Increased from 40
    cell_width=50,  # Adjusted based on the new font size
    cell_height=70,  # Adjusted based on the new font size
    background_color=(40, 40, 40, 255),
    show_line_numbers=True,
)
# frame = frame_generator.generate_image(grid_obj)


def main():
    os.system("rm frames/*")
    video_path = "clips/output_video.mp4"

    # Read the code from a file
    with open("src/source_code.py", "r") as file:
        code_string = file.read()

    grid_obj = Grid()
    grid_obj.insert_highlighted(code_string)

    video = Video(video_path, grid_obj, cell_width=15, cell_height=40, font_size=30)
    for i in range(0, 10):
        video.animation_queue.add_visual_effect(
            FadeIn(start_frame=0, end_frame=40, line_number=i, persist_duration=20)
        )
        video.animation_queue.add_visual_effect(
            WipeLine(
                start_frame=60,
                end_frame=80,
                line_number=i,
                persist_duration=0,
            )
        )
        video.animation_queue.add_grid_effect(
            UpdateLineContent(
                start_frame=81,
                end_frame=81,
                line_number=i,
                new_content=f"line{str(i)}!!!",
                persist_duration=300,
            )
        )
        video.animation_queue.add_visual_effect(
            TypingEffect(
                start_frame=82,
                end_frame=120,
                line_number=i,
                persist_duration=100,
            )
        )

    # Record the start time
    start_time = time.time()

    # Render the video
    video.render_video(grid_obj, duration=10, fps=30)

    # Calculate and print the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Video rendering took {elapsed_time} seconds")

    # Delete all files in frames folder
    # os.system("rm frames/*")


if __name__ == "__main__":
    main()
