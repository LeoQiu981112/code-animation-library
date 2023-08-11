from src.image_generator import ImageGenerator
from src.animations import Animation, AnimationQueue
from src.grid import Grid
from multiprocessing import Pool
import numpy as np
import imageio
import copy
from typing import List, Tuple
import logging


class Video:
    """
    Class for managing the video stream.
    """

    BACKGROUND_COLOR = (40, 40, 40, 255)

    def __init__(
        self,
        path: str,
        grid_obj: Grid,
        cell_width: int = 40,
        cell_height: int = 60,
        font_size: int = 50,
    ):
        self.output_path = path
        self.grid_obj = grid_obj
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.font_size = font_size
        self.animation_queue: AnimationQueue = AnimationQueue()

        self.frame_generator = ImageGenerator(
            font_size=self.font_size,
            cell_width=self.cell_width,
            cell_height=self.cell_height,
            background_color=self.BACKGROUND_COLOR,
            show_line_numbers=True,
        )
        self.DEBUG_FRAME = 110

    def configure_logging(self, enable=True):
        if enable:
            logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        else:
            logging.disable(logging.CRITICAL)

    def debug_log(self, frame_index: int, message: str):
        if frame_index == self.DEBUG_FRAME:
            logging.debug(message)

    def generate_frame(
        self,
        frame_index: int,
        grid_obj: Grid,
        grid_states: List[Animation],
        visual_states: List[Animation],
    ) -> np.ndarray:
        self.configure_logging(enable=False)
        grid_copy: Grid = self.prepare_grid_copy(
            grid_obj, frame_index, grid_states, visual_states
        )
        frame = self.frame_generator.generate_image(grid_copy)
        return np.array(frame)

    def prepare_grid_copy(
        self,
        grid_obj: Grid,
        frame_index: int,
        grid_states: List[Animation],
        visual_states: List[Animation],
    ) -> Grid:
        grid_copy: Grid = copy.deepcopy(grid_obj)

        for animation in grid_states[frame_index]:
            self.debug_log(frame_index, f"before grid_states {animation}")
            animation.apply(grid_copy, frame_index)
            self.debug_log(frame_index, f"after grid_states {animation}")
        for animation in visual_states[frame_index]:
            animation.apply(grid_copy, frame_index)
        return grid_copy

    def render_video(
        self,
        grid_obj: Grid,
        duration: float,
        output_filename: str = "output.mp4",
        fps: int = 30,
    ) -> str:
        """
        Renders the video to the specified output file.
        """
        num_frames = int(duration * fps)
        (
            visual_frame_states,
            grid_frame_states,
        ) = self.animation_queue.compute_animation_states(duration, fps)
        self.configure_logging(enable=True)
        args = [
            (frame_index, grid_obj, grid_frame_states, visual_frame_states)
            for frame_index in range(num_frames)
        ]

        with Pool() as pool:
            frames = pool.starmap(self.generate_frame, args)

        with imageio.get_writer(
            output_filename, fps=fps, codec="libx264", bitrate="8000k"
        ) as writer:
            for frame in frames:
                writer.append_data(frame)

        return output_filename
