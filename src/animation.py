from typing import List, Tuple, Type
from abc import ABC, abstractmethod


class Animation(ABC):
    def __init__(self, start_time, duration):
        self.start_time = start_time
        self.duration = duration

    @abstractmethod
    def apply(self, grid, current_time):
        """
        Apply the animation to a copy of the grid and return it.

        The exact behavior of this method should be implemented by subclasses.
        """
        pass

    def is_active(self, current_time):
        """
        Check whether the animation is active at the given time.
        """
        return 0 <= current_time < self.duration


class FadeIn(Animation):
    """
    Animation class for fading in an entire line in the grid.
    """

    def __init__(self, start_time, duration, line_number):
        """
        Initialize the FadeInAnimation instance.

        Args:
            start_time (float): The start time of the animation (in seconds).
            duration (float): The duration of the animation (in seconds).
            line_number (int): The line number to fade in.
        """
        self.line_number = line_number
        super().__init__(start_time, duration)

    def apply(self, grid, current_time):
        """
        Apply the fade-in animation to the grid.

        Args:
            grid (Grid): The grid on which the animation will be applied.
            current_time (float): The current time of the video (in seconds).

        Returns:
            List[List[str]]: The updated grid after applying the animation.
        """
        if not self.is_active(current_time):
            return grid

        line_str, line_token_colors = grid.line(self.line_number)

        # Apply the fade-in effect to the entire line by increasing the transparency of each character
        faded_line_str = []
        for char in line_str:
            # Modify the character (e.g., with the faded version) to represent the fade-in effect
            # Adjust the transparency/alpha of the color (e.g., increase alpha to fade-in)
            faded_line_str.append(char)

        # Update the grid with the modified faded line
        grid.grid[self.line_number] = faded_line_str
        return grid.grid


class AnimationQueue:
    def __init__(self):
        self.animations = []

    def add_animation(self, animation):
        if isinstance(animation, Animation):
            self.animations.append(animation)
        else:
            raise TypeError("Only Animation instances can be added to the AnimationQueue.")

    def extend(self, animations):
        for animation in animations:
            if isinstance(animation, Animation):
                self.animations.append(animation)
            else:
                raise TypeError("Only Animation instances can be added to the AnimationQueue.")

    def apply_animations(self, grid, current_time):
        """
        Apply all animations that are active at the given time to the grid.
        """
        for animation in self.animations:
            if animation.is_active(current_time):
                grid = animation.apply(grid, current_time)
        return grid

    def get_duration(self):
        """
        Get the maximum duration of any animation in the queue.
        """
        return max(animation.duration for animation in self.animations)