from abc import ABC, abstractmethod
from src.tokenizer import CodeTokenizer
from src.character import Character
import copy


# Animation Classes
class Animation(ABC):
    def __init__(self, start_time, duration):
        self.start_time = start_time
        self.duration = duration

    @abstractmethod
    def apply(self, grid, current_time):
        pass

    def is_active(self, current_time):
        return self.start_time <= current_time < self.start_time + self.duration


class TypingEffect(Animation):
    def __init__(self, start_time, duration, line_number):
        super().__init__(start_time, duration)
        self.line_number = line_number
        self.original_colors = None  # Store the original colors here

    def apply(self, grid_obj, current_time):
        if not self.is_active(current_time):
            return

        # Get the line
        line = grid_obj.get_line(self.line_number)

        # If this is the first time the animation is being applied, store the original colors
        if self.original_colors is None:
            self.original_colors = [char.color for char in line]
            for char in line:
                char.color = (40, 40, 40, 255)  # Make all characters transparent

        # Calculate how many characters should be visible based on the current time
        proportion_done = max(0, (current_time - self.start_time) / self.duration)
        num_chars = int(proportion_done * len(line))

        # Change the color of the appropriate number of characters back to their original color
        for i in range(num_chars):
            line[i].color = self.original_colors[i]


class FadeIn(Animation):
    def __init__(self, start_time, duration, line_number, start_color=(40, 40, 40)):
        super().__init__(start_time, duration)
        self.line_number = line_number
        self.start_color = start_color

    def apply(self, grid_obj, current_time):
        if not self.is_active(current_time):
            return

        progress = max(0, (current_time - self.start_time) / self.duration)

        line = grid_obj.get_line(self.line_number)

        for character in line:
            end_color = character.color
            current_color = tuple(
                start + int((end - start) * progress)
                for start, end in zip(self.start_color, end_color[:3])
            )

            if len(self.start_color) == 3:
                current_color += (255,)

            character.color = current_color


class FadeOut(Animation):
    def __init__(self, start_time, duration, line_number, end_color=(40, 40, 40)):
        super().__init__(start_time, duration)
        self.line_number = line_number
        self.end_color = end_color

    def apply(self, grid_obj, current_time):
        if not self.is_active(current_time):
            return

        progress = max(0, (current_time - self.start_time) / self.duration)

        line = grid_obj.get_line(self.line_number)

        for character in line:
            start_color = character.color
            current_color = tuple(
                start + int((end - start) * progress)
                for start, end in zip(start_color[:3], self.end_color)
            )

            if len(self.end_color) == 3:
                current_color += (255,)

            character.color = current_color


# AnimationQueue Class
class AnimationQueue:
    def __init__(self):
        self.animations = []

    def add_animation(self, animation):
        if not isinstance(animation, Animation):
            raise TypeError(
                "Only Animation instances can be added to the AnimationQueue."
            )
        self.animations.append(animation)

    def extend(self, animations):
        if not all(isinstance(animation, Animation) for animation in animations):
            raise TypeError(
                "Only Animation instances can be added to the AnimationQueue."
            )
        self.animations.extend(animations)

    def apply_animations(self, grid, current_time):
        for animation in self.animations:
            if animation.is_active(current_time):
                animation.apply(grid, current_time)

    def get_duration(self):
        return max(animation.duration for animation in self.animations)


# Grid Class
class Grid:
    def __init__(self):
        self.grid = [[]]
        self.tokenizer = CodeTokenizer("python")
        self.animation_queue = AnimationQueue()

    def add_line(self):
        self.grid.append([])

    def set_line(self, line_number, line):
        self.grid[line_number] = line

    def add_character(self, char, token_type, color, position):
        character = Character(char, token_type, color, position)
        self.grid[-1].append(character)

    def insert_highlighted(self, text):
        self.tokenizer.tokenize(self, text)

    def get_line(self, line_number):
        return self.grid[line_number]

    def apply_animations(self, current_time):
        for animation in self.animation_queue.animations:
            if animation.is_active(current_time):
                animation.apply(self, current_time)

    def copy(self):
        grid_copy = Grid()
        grid_copy.grid = copy.deepcopy(self.grid)
        grid_copy.tokenizer = self.tokenizer
        return grid_copy
