from src.image_generator import ImageGenerator
from src.animations import AnimationQueue
from src.grid import Grid
from multiprocessing import Pool
from functools import partial
import numpy as np  # Don't forget to import numpy
import time
import imageio
import copy


class Video:
    """
    Class for managing the video stream.
    """

    def __init__(self, path):
        self.output_path = path
        # tweak later
        self.cell_width = 20
        self.cell_height = 20
        self.font_size = 20
        self.background_color = (40, 40, 40, 255)

        self.frame_generator = ImageGenerator(
            font_size=self.font_size,
            cell_width=self.cell_width,
            cell_height=self.cell_height,
            background_color=(40, 40, 40, 255),
        )

        self.animations = AnimationQueue()

    def add_animation(self, *args):
        self.animations.extend(args)
        print("test:", self.animations, "\n\n")

    # def generate_frame(self, frame_index, grid_obj, fps):
    #     """
    #     Generate and return a single frame of the video.

    #     Parameters:
    #         frame_index (int): The index of the current frame (starts from 0).
    #         grid_obj (Grid): The Grid object representing the state of the animation.

    #     Returns:
    #         frame (numpy.ndarray): The generated frame as a NumPy array (image).
    #     """
    #     grid_copy = copy.deepcopy(grid_obj)
    #     current_time = frame_index / fps
    #     grid_copy.apply_animations(current_time)
    #     frame = self.frame_generator.generate_image(grid_copy)
    #     # frame.save(f"frames/frame_{frame_index}.png")
    #     return frame

    def generate_frame(self, frame_index, grid_obj, fps):
        grid_copy = copy.deepcopy(grid_obj)
        current_time = frame_index / fps
        grid_copy.apply_animations(current_time)
        frame = self.frame_generator.generate_image(grid_copy)
        frame_np = np.array(frame)  # Convert the PIL.Image object to a numpy array
        return frame_np

        # def render_video(self, grid_obj, duration, output_filename="output.mp4", fps=30):
        # num_frames = int(duration * fps)  # Calculate the total number of frames
        # p = Pool()
        # generate_frame_partial = partial(
        #     self.generate_frame, grid_obj=grid_obj, fps=fps
        # )
        # frames = p.map(generate_frame_partial, range(num_frames))
        # p.close()
        # p.join()

        # # Save the frames as a video using imageio.mimsave
        # imageio.mimsave(output_filename, frames, fps=fps, bitrate="5000k")
        # return output_filename

    def render_video(self, grid_obj, duration, output_filename="output.mp4", fps=30):
        num_frames = int(duration * fps)  # Calculate the total number of frames
        p = Pool()
        generate_frame_partial = partial(
            self.generate_frame, grid_obj=grid_obj, fps=fps
        )
        frames = p.map(generate_frame_partial, range(num_frames))
        p.close()
        p.join()

        # Save the frames as a video using imageio.get_writer
        with imageio.get_writer(
            output_filename, fps=fps, codec="libx264", bitrate="5000k"
        ) as writer:
            for frame in frames:
                writer.append_data(frame)

        return output_filename
