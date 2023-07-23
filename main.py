from src.tokenizer import CodeTokenizer
from src.image_generator import ImageGenerator

with open("src/source_code.py", "r") as file:
    # Read the file
    code_string = file.read()

with open("src/banner.py", "r") as file:
    # Read the file
    banner_string = file.read()
# Now, code_string contains the contents of the file

language = "python"
tokenizer = CodeTokenizer(code_string, language)
tokenizer.populate_grid()

# Get the grid of characters and their types
grid = tokenizer.get_grid()
# Create an ImageGenerator instance and generate the image
frame_generator = ImageGenerator(
    grid, font_size=20, cell_width=15, cell_height=35, background_color=(40, 40, 40)
)
frame = frame_generator.generate_image()
frame.save("code_image.png", dpi=(100, 100))


banner_tokenizer = CodeTokenizer(banner_string, language)
print(banner_string)
banner_tokenizer.populate_grid()
banner_grid = banner_tokenizer.get_grid()  # Use banner_tokenizer's grid here
print(banner_grid)
# CREATE SEPARATE GENERATOR FOR YOUTUBE BANNER
banner_generator = ImageGenerator(
    banner_grid, font_size=50, cell_width=55, cell_height=55, background_color=(36, 41, 46))

banner = banner_generator.generate_image()

# Save the image to a file
banner.save("banner_image.png", dpi=(100, 100))
