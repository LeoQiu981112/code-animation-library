# Code Animation Library

The Code Animation Library is a Python library that allows you to create animated visualizations of code snippets. It utilizes Pygments for syntax highlighting and PIL (Python Imaging Library) for image manipulation.

## Features

- Convert code snippets into animated images or video.
- Syntax highlighting using Pygments.
- Customizable styles for code highlighting.
- Support for various animation effects, such as zooming, scrolling, and highlighting.

## workflow:

- The Grid class represents the state of the code with characters, token types, and animations.
- The Animation classes, such as FadeIn, define the animations that can be applied to the Grid.
- The AnimationQueue class manages the collection of animations to apply to the Grid.
- The ImageGenerator class takes a Grid instance and creates an image representation of the code with colors applied based on token types.
- The Video class manages the frame generation by applying animations from the AnimationQueue to the Grid and then generating and saving frames using imageio.mimsave.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/code-animation-library.git

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