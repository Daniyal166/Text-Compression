Image to Text Conversion and Vice Versa
This repository contains two Python scripts that can convert images to text and vice versa. The scripts use the Python Imaging Library (PIL) to manipulate images and text files.

Image to Text Conversion
The imageToText.py script converts a greyscale image to a text file. The text file contains ASCII characters that represent the pixel values of the image.

Function Reference
greyscale_image_to_text(input_image, output_text): Converts a greyscale image to a text file.
Example Usage
To convert a greyscale image to a text file, run the following command:

Copy code
python imageToText.py greyscale_image.png output_text.txt
Text to Image Conversion
The textToImage.py script converts a text file to a greyscale image. The image contains pixel values that represent the ASCII values of the characters in the text file.

Function Reference
get_file_size(file_path): Returns the size of a file in bytes.
text_to_greyscale_image(input_file, output_image): Converts a text file to a greyscale image.
Example Usage
To convert a text file to a greyscale image, run the following command:

Copy code
python textToImage.py 5mb.txt greyscale_image.png
The script will print the sizes of the original text file and the generated image file.



Scroll to bottom

