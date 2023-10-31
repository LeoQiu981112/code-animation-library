from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Union, Dict
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.grid import Grid
HIGHLIGHT_COLOR = (255, 255, 0, 255)
TRANSPARENT_COLOR = (40, 40, 40, 0)


class Animation(ABC):
    """
    Abstract base class for all animations.
    """

    def __init__(self, start_frame, end_frame):
        self.start_frame = start_frame
        self.end_frame = end_frame

    @abstractmethod
    def apply(self, grid: "Grid", current_time: float) -> None:
        """
        Apply the animation on the grid at the given time.

        Parameters:
        grid (Grid): The grid on which to apply the animation.
        current_time (float): The current time.
        """
        pass

    def persist(self, grid: "Grid") -> None:
        """
        Persist the final state of the animation on the grid.
        """
        pass

    def is_active(self, frame_index: int) -> bool:
        """
        Return True if the animation is active at the given frame index.
        """
        return self.start_frame <= frame_index <= self.end_frame

    def is_finished(self, frame_index: int) -> bool:
        """
        Return True if the animation is finished at the given frame index.
        """
        return frame_index > self.end_frame


class VisualEffect(Animation):
    """Base class for all visual effects."""

    def __init__(
        self,
        start_frame: int,
        end_frame: int,
        line_number: int,
        start_index: Optional[int] = None,
        end_index: Optional[int] = None,
        persist_duration: int = 0,
    ):
        super().__init__(start_frame, end_frame)
        self.line_number = line_number
        self.start_index = start_index
        self.end_index = end_index
        self.persist_duration = persist_duration


class GridEffect(Animation):
    """Base class for all grid-changing effects."""

    def __init__(
        self,
        start_frame: int,
        end_frame: int,
        line_number: int,
        start_index: Optional[int] = None,
        end_index: Optional[int] = None,
        persist_duration: int = 0,
    ):
        super().__init__(start_frame, end_frame)
        self.line_number = line_number
        self.start_index = start_index
        self.end_index = end_index
        self.persist_duration = persist_duration


class AnimationQueue:
    """
    A queue of animations to be applied on the grid.
    """

    def __init__(self):
        self.visual_effects: List[VisualEffect] = []
        self.grid_effects: List[GridEffect] = []

    def add_visual_effect(self, effect: VisualEffect) -> None:
        self.visual_effects.append(effect)

    def add_grid_effect(self, effect: GridEffect) -> None:
        self.grid_effects.append(effect)

    def compute_animation_states(self, duration: float, fps: float):
        """
        Compute and return animations states for each frame.
        """
        total_frames = int(duration * fps)
        visual_frame_states, grid_frame_states = [], []

        def compute_frame_states(animations):
            frame_states = []
            for frame_index in range(total_frames):
                active_animations = []
                for animation in animations:
                    if animation.is_active(frame_index) or (
                        animation.is_finished(frame_index)
                        and frame_index
                        <= animation.end_frame + animation.persist_duration
                    ):
                        active_animations.append(animation)
                frame_states.append(active_animations)
            return frame_states

        visual_frame_states = compute_frame_states(self.visual_effects)
        grid_frame_states = compute_frame_states(self.grid_effects)
        return visual_frame_states, grid_frame_states


class FadeIn(VisualEffect):
    def __init__(
        self,
        start_frame: int,
        end_frame: int,
        line_number: int,
        start_color: Tuple[int, int, int, int] = TRANSPARENT_COLOR,
        persist_duration: int = 0,
    ):
        super().__init__(
            start_frame, end_frame, line_number, persist_duration=persist_duration
        )
        self.start_color = start_color
        self.final_colors = None

    @staticmethod
    def ease_in_quad(x):
        return x * x

    @staticmethod
    def calculate_color(progress, start_color, end_color):
        """
        Calculate the color at the given progress between the start and end colors.
        color is a tuple of (r, g, b, a) values.
        """
        return tuple(
            int(start_val + (end_val - start_val) * progress)
            for start_val, end_val in zip(start_color, end_color)
        )

    def apply(self, grid_obj: "Grid", frame_index: int) -> None:
        line = grid_obj.get_line(self.line_number)
        if self.is_active(frame_index):
            total_frames = self.end_frame - self.start_frame
            frames_elapsed = frame_index - self.start_frame
            linear_progress = max(0, frames_elapsed / total_frames)
            progress = self.ease_in_quad(linear_progress)
            for char in line.iter_characters():
                char.set_visibility(True)
                target_color = char.get_color()
                current_color = self.calculate_color(
                    progress, self.start_color, target_color
                )
                char.set_color(current_color)
            # print(f"fade in at frame, {frame_index}")
        elif (
            self.is_finished(frame_index)
            and frame_index <= self.end_frame + self.persist_duration
        ):
            # print(
            #     f"Persisting fade-in effect for line {self.line_number} at frame {frame_index}"
            # )
            for char in line.iter_characters():
                char.set_visibility(True)


class WipeLine(VisualEffect):
    def __init__(
        self,
        start_frame: int,
        end_frame: int,
        line_number: int,
        wipe_mode: str = "opacity",  # Can be either "opacity" or "space"
        persist_duration: int = 0,
        target_color: Tuple[int, int, int, int] = (40, 40, 40, 0),  # Background color
    ):
        super().__init__(
            start_frame, end_frame, line_number, persist_duration=persist_duration
        )
        self.wipe_mode = wipe_mode
        self.target_color = target_color

    def apply(self, grid_obj: "Grid", frame_index: int) -> None:
        if self.is_active(frame_index):
            # print(f"wipe line at frame, {frame_index}")
            line = grid_obj.get_line(self.line_number)
            total_frames = self.end_frame - self.start_frame
            frames_elapsed = frame_index - self.start_frame
            linear_progress = max(0, min(frames_elapsed / total_frames, 1))

            # Apply the wipe effect based on the selected mode
            if self.wipe_mode == "opacity":
                for char in line.iter_characters():
                    char.set_visibility(True)
                    start_color = char.get_color()
                    current_color = tuple(
                        start + int((end - start) * linear_progress)
                        for start, end in zip(start_color, self.target_color)
                    )
                    char.set_color(current_color)
        elif (
            self.is_finished(frame_index)
            and frame_index <= self.end_frame + self.persist_duration
        ):
            # print(f"Persisting wipe effect at frame {frame_index}")
            line = grid_obj.get_line(self.line_number)
            if self.wipe_mode == "opacity":
                for char in line.iter_characters():
                    char.set_visibility(True)
                    char.set_color(self.target_color)
            # Additional logic for persisting the "space" mode


class UpdateLineContent(GridEffect):
    def __init__(
        self,
        start_frame: int,
        end_frame: int,
        line_number: int,
        new_content: str,
        persist_duration: int = 0,
    ):
        super().__init__(
            start_frame, end_frame, line_number, persist_duration=persist_duration
        )
        # self.line_number = line_number
        self.new_content = new_content
        # self.persist_duration = persist_duration

    def apply(self, grid_obj: "Grid", frame_index: int) -> None:
        if self.is_active(frame_index) or (
            self.is_finished(frame_index)
            and frame_index <= self.end_frame + self.persist_duration
        ):
            # print(f"UpdateLineContent at frame, {frame_index}")
            line = grid_obj.get_line(self.line_number)
            line.tokens = []
            grid_obj.tokenizer.tokenize_line(line, self.new_content)


class TypingEffect(VisualEffect):
    def __init__(
        self,
        start_frame: int,
        end_frame: int,
        line_number: int,
        persist_duration: int = 0,
    ):
        super().__init__(start_frame, end_frame, line_number)
        self.persist_duration = persist_duration
        self.total_frames = end_frame - start_frame

    def apply(self, grid_obj: "Grid", frame_index: int) -> None:
        if self.is_active(frame_index):
            # print(f"TypingEffect at frame, {frame_index}")
            line = grid_obj.get_line(self.line_number)
            total_chars = sum(len(token.characters) for token in line.tokens)
            chars_to_display = int(
                ((frame_index - self.start_frame) / self.total_frames) * total_chars
            )

            char_counter = 0
            for char in line.iter_characters():
                if char_counter < chars_to_display:
                    char.set_visibility(True)
                char_counter += 1
        elif (
            self.is_finished(frame_index)
            and frame_index <= self.end_frame + self.persist_duration
        ):
            # print(f"Persisting TypingEffect effect at frame {frame_index}")
            self.persist(grid_obj)

    def persist(self, grid: "Grid") -> None:
        line = grid.get_line(self.line_number)
        for token in line:
            token.set_visibility(True)


class MoveLine(VisualEffect):
    def __init__(
        self, line_number, target_line_number, start_frame, end_frame, persist_duration
    ):
        super().__init__(start_frame, end_frame, line_number)
        self.target_line_number = target_line_number
        self.persist_duration = persist_duration

    @staticmethod
    def ease_in_quad(x):
        return x * x

    def apply(self, grid_copy: "Grid", frame_index):
        if self.is_active(frame_index):
            linear_progress = (frame_index - self.start_frame) / (
                self.end_frame - self.start_frame
            )
            progress = self.ease_in_quad(linear_progress)
            offset = (self.target_line_number - self.line_number) * progress
            line = grid_copy.get_line(self.line_number)
            for character in line.iter_characters():
                character.set_visibility(True)
                character.position.y += offset
        elif (
            self.is_finished(frame_index)
            and frame_index <= self.end_frame + self.persist_duration
        ):
            self.persist(grid_copy)

    def persist(self, grid: "Grid") -> None:
        # characters should have the same offset as the last active frame
        offset = self.target_line_number - self.line_number
        line = grid.get_line(self.line_number)
        for character in line.iter_characters():
            character.set_visibility(True)
            character.position.y += offset


class BlinkEffect(VisualEffect):
    pass


class ScrollToLine(Animation):
    def __init__(self, start_time: float, end_time: float, target_line: int):
        super().__init__(start_time, end_time)
        self.target_line = target_line
        self.start_time = start_time
        self.end_time = end_time
        self.previous_scroll_amount = 0

    def get_progress(self, current_time: float) -> float:
        """
        Calculate the progress of the animation.

        Parameters:
        current_time (float): The current time.

        Returns:
        float: The progress of the animation.
        """
        total_duration = self.end_time - self.start_time
        elapsed_time = current_time - self.start_time
        return min(max(elapsed_time / total_duration, 0), 1)

    def apply(self, grid: "Grid", current_time: float) -> None:
        """
        Apply the animation on the grid at the given time.

        Parameters:
        grid (Grid): The grid on which to apply the animation.
        current_time (float): The current time.
        """
        progress = self.get_progress(current_time)

        # Use an easing function to calculate the scroll amount
        scroll_amount = self.easeInOutQuad(progress) * self.target_line

        diff = scroll_amount - self.previous_scroll_amount
        int_diff = round(diff)
        self.previous_scroll_amount += int_diff

        for line in grid.grid:
            # for character in line:
            #     character.position.y -= int_diff
            line.move(0, -int_diff)

    @staticmethod
    def easeInOutQuad(t: float) -> float:
        """
        A simple easing function that accelerates at the start and decelerates at the end.

        Parameters:
        t (float): The progress of the animation.

        Returns:
        float: The result of the easing function.
        """
        if t < 0.5:
            return 2 * t * t
        else:
            return -1 + (4 - 2 * t) * t


class Highlight(Animation):
    def __init__(
        self,
        start_time: float,
        duration: float,
        line_number: int,
        start_index: Optional[int] = None,
        end_index: Optional[int] = None,
        color: Tuple[int, int, int, int] = (255, 255, 0, 255),
    ):
        super().__init__(start_time, duration)
        self.line_number = line_number
        self.start_index = start_index
        self.end_index = end_index
        self.color = color

    def apply(self, grid_object: "Grid", current_time: float) -> None:
        """
        Apply the animation on the grid at the given time.

        Parameters:
        grid_object (Grid): The grid on which to apply the animation.
        current_time (float): The current time.
        """
        if not self.is_active(current_time):
            return

        line = grid_object.get_line(self.line_number)

        # If start_index and end_index are None, highlight the entire line
        if self.start_index is None and self.end_index is None:
            for character in line:
                character.color = self.color
        else:  # Otherwise, highlight the specified range
            for character in line[self.start_index : self.end_index]:
                character.color = self.color
