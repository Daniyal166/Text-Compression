import os
from PIL import Image

def get_file_size(file_path):
    return os.path.getsize(file_path)

def text_to_greyscale_image(input_file, output_image):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Create an image with width based on the length of the text and height of 1
    image_width = len(text)
    image = Image.new('L', (image_width, 1))

    # Set pixel values based on ASCII values of characters
    for i in range(image_width):
        pixel_value = ord(text[i])
        image.putpixel((i, 0), pixel_value)

    # Save the greyscale image
    image.save(output_image)

    # Print the sizes of the original text file and the generated image file
    original_text_size = get_file_size(input_file)
    generated_image_size = get_file_size(output_image)

    print(f"Size of the original text file '{input_file}': {original_text_size} bytes")
    print(f"Size of the generated greyscale image file '{output_image}': {generated_image_size} bytes")

# Example usage
text_file_path = '5mb.txt'
greyscale_image_path = 'greyscale_image.png'

text_to_greyscale_image(text_file_path, greyscale_image_path)
