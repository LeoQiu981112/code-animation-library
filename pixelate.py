from PIL import Image


# can be used as intro/outro
def pixelate_image(image_path, pixel_size):
    # Open the image
    image = Image.open(image_path)

    # Calculate the new image dimensions with pixelation
    new_width = image.width // pixel_size
    new_height = image.height // pixel_size

    # Resize the image to the new dimensions using NEAREST resampling
    pixelated_image = image.resize((new_width, new_height), Image.NEAREST)

    # Resize the pixelated image back to the original dimensions using NEAREST resampling
    pixelated_image = pixelated_image.resize(image.size, Image.NEAREST)

    return pixelated_image


if __name__ == "__main__":
    input_image_path = "code_image.png"  # Replace with the path to your input image
    pixel_size = 10  # Set the pixel size for pixelation

    pixelated_image = pixelate_image(input_image_path, pixel_size)

    # Save the pixelated image
    output_image_path = "code_image1.png"  # Replace with the desired output path
    pixelated_image.save(output_image_path)
