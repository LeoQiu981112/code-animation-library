from tokenizer import CodeTokenizer
from image_generator import ImageGenerator


with open("code_to_run.py", "r") as file:
    # Read the file
    code_string = file.read()

# Now, code_string contains the contents of the file
print(code_string)

language = "python"
tokenizer = CodeTokenizer(code_string, language)
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
image.save("code_image.png", dpi=(1200, 1200))
