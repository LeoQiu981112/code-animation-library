from src.image_generator import ImageGenerator
from src.animation import AnimationQueue
from src.grid import Grid
from multiprocessing import Pool
from functools import partial
import time
import imageio


class Video:
    """
    Class for managing the video stream.
    """
    def __init__(self, path):
        self.output_path = path
        self.fps = 30
        # tweak later
        self.cell_width = 10
        self.cell_height = 20
        self.font_size = 15
        self.background_color = (40, 40, 40)
        self.frame_generator = ImageGenerator(font_size=20, cell_width=15, cell_height=35, background_color=(40, 40, 40))
        self.animations = AnimationQueue()

    def add_animation(self, *args):
        self.animations.extend(args)
        print("test:", self.animations, "\n\n")

    def generate_frame(self, frame_index, grid_obj):
        """
        Generate and return a single frame of the video.

        Parameters:
            frame_index (int): The index of the current frame (starts from 0).
            grid_obj (Grid): The Grid object representing the state of the animation.

        Returns:
            frame (numpy.ndarray): The generated frame as a NumPy array (image).
        """
        # Calculate the current time based on the frame index and frame rate (fps)
        current_time = frame_index / self.fps

        # Apply animations from the AnimationQueue to the grid based on the current time
        grid_obj.apply_animations(current_time)

        # Draw the grid onto the frame
        frame = grid_obj.draw()

        # You can add any additional drawings, overlays, text, etc., to the frame as needed.

        # Simulate some processing time to make the frame generation time-consuming
        time.sleep(0.1)  # Replace this with your actual rendering code

        return frame

    def render_video(self, grid_obj, num_frames, output_filename="output.mp4", fps=30):
        p = Pool()
        generate_frame_partial = partial(self.generate_frame, grid_obj=grid_obj)
        frames = p.map(generate_frame_partial, range(num_frames))
        p.close()
        p.join()

        # Save the frames as a video using imageio.mimsave
        imageio.mimsave(output_filename, frames, fps=fps)

        return output_filename

