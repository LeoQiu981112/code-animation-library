from pygments.style import Style
from pygments.token import Comment, Keyword, Name, String, Error, Number, Operator
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter


class NordStyle(Style):
    default_style = ""
    styles = {
        Comment:                '#81a1c1',    # Comment style
        Keyword:                'bold #81a1c1',    # Keyword style
        Name:                   '#81a1c1',    # Name style
        String:                 '#a3be8c',    # String style
        Error:                  '#bf616a',    # Error style
        Number:                 '#b48ead',    # Number style
        Operator:               '#81a1c1',    # Operator style
        # Add more token styles as desired
    }


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

# lexer = get_lexer_by_name('python')
# formatter = TerminalFormatter(style=NordStyle)

# highlighted_code = highlight(code, lexer, formatter)
# print(highlighted_code)
