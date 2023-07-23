from src.tokenizer import CodeTokenizer
from src.image_generator import ImageGenerator


with open("src/source_code.py", "r") as file:
    # Read the file
    code_string = file.read()

# Now, code_string contains the contents of the file

language = "python"
tokenizer = CodeTokenizer(code_string, language)
tokenizer.populate_grid()

# Get the grid of characters and their types
grid = tokenizer.get_grid()
# Create an ImageGenerator instance and generate the image
generator = ImageGenerator(
    grid, font_size=20, cell_width=15, cell_height=35, background_color=(40, 40, 40)
)
image = generator.generate_image()

# Save the image to a file
image.save("code_image.png", dpi=(100, 100))
