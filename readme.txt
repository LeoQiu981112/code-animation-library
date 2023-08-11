---

# Code Animation Library 🎞️💻

The Code Animation Library is a Python library that allows you to create animated visualizations of code snippets. It utilizes Pygments for syntax highlighting and PIL (Python Imaging Library) for image manipulation.

## Features 🔥

- Convert code snippets into animated images or video. 🖼️🎥
- Syntax highlighting using Pygments. 🌈
- Customizable styles for code highlighting. 🎨
- Support for various animation effects, such as zooming, scrolling, and highlighting. ✨

## Installation 💾

1. Clone the repository:

   ```shell
   git clone https://github.com/LeoQiu981112/code-animation-library.git
   ```

   cd code-animation-library
   ```
2. Install the required packages:

   ```shell
   pip install -r requirements.txt
   ```
3. Run the code animation library:

   ```shell
   python3 main.py
   ```

## Patch Notes 📝

### Version 0.4 (Latest) 🚀

- **Enhanced Video Class**: Introduced improvements in the `Video` class, including optimized multiprocessing, refactoring, and logging.
- **Animation Queue Management**: Moved animation queue out of the grid and split visual and grid effects for better control.
- **Precomputed Animations**: Implemented a new system to precompute animations that need to be applied, enhancing efficiency in frame generation.
- **Enhanced Grid Handling**: Preallocated lines in the grid and optimized grid copying, improving efficiency and maintainability.
- **Debugging Enhancements**: Fixed issues related to fade-in animation and added logging for better debugging and development.
- **Performance Optimization**: Reduced video rendering time and made significant strides in optimizing the library's overall performance.
- **Updated font to use Mono
- **Upcoming Features**:
  - **Advanced Visual Effects**: Explore new effects like zooming, scrolling, highlighting, and more.
  - **Integration with Tools**: Consider integration with tools like Premiere Pro for advanced editing.
  - **Performance Optimization**: Continue to focus on enhancing rendering performance and user experience.

### Version 0.3 🚀

- **Added `Character` class**: This class represents a character in the code. Each character has a token type, color (now in RGBA), and position.

- **Added `Animation` class**: This class serves as a base for different animation effects. Each animation has a start time, end time, and methods to determine if the animation is active and to apply the animation.

- **Added RGBA colors**: Colors are now represented in RGBA (Red, Green, Blue, Alpha), allowing for transparency effects.

- **Grid updated to be numpy compatible**: This update allows for more efficient manipulation and processing of the grid.

- **Added Video class**: This class manages the generation of video frames.

- **Added support for custom colors and fonts**: You can now customize the appearance of your code with different colors and fonts.

- **Code refactor and style update**: The code has been refactored for better organization and readability, and the style has been updated.

- **Debugging Fade In**: Fixed issues related to the Fade In animation.

- **Upcoming Features**:
  - **Zooming In/Out**: This feature will allow you to zoom in and out on specific parts of the code.
  - **Scrolling**: This feature will allow you to scroll the code up and down.
  - **Highlighting**: This feature will allow you to highlight specific lines or characters in the code.
  - **Pixel Art Avatars**: This feature will allow you to add pixel art avatars to your animations.
  - **Dynamic Conversation/Dialogue**: This feature will allow you to add conversation or dialogue to your animations.
  - **Cursor**: This feature will allow you to add a cursor to your animations, simulating the typing of the code and guiding the viewer's attention. Used in combination with the highlighting feature, it will provide clear visual guidance for viewers to follow along with the code.

---