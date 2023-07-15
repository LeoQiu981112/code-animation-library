from tokenizer import CodeTokenizer
from image_generator import ImageGenerator


code = """from typing import List, Tuple
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import RawTokenFormatter
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
from pygments.styles import get_style_by_name
import webcolors
from pygments.token import Token

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

        test = dict()
        for i in range(len(nums)):
            if target - nums[i] in test:
                    return [test[target - nums[i]], i]
            test[nums[i]] = i
        return [-1,-1]
"""
language = "python"
tokenizer = CodeTokenizer(code, language)
tokenizer.populate_grid()

# Get the grid of characters and their types
grid = tokenizer.get_grid()
# Create an ImageGenerator instance and generate the image
generator = ImageGenerator(
    grid, font_size=20, cell_width=15, cell_height=35, background_color=(30, 30, 30)
)
image = generator.generate_image()

# Save the image to a file
image.show()
# image.save("code_image.png", dpi=(1200, 1200))
