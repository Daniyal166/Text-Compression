from PIL import Image

def greyscale_image_to_text(input_image, output_text):
    # Open the greyscale image
    image = Image.open(input_image)

    # Get the width of the image
    image_width = image.width

    # Retrieve pixel values and convert them back to ASCII characters
    text = ''.join([chr(image.getpixel((i, 0))) for i in range(image_width)])

    # Save the text to a file
    with open(output_text, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage
greyscale_image_to_text('greyscale_image.png', 'output_text.txt')
