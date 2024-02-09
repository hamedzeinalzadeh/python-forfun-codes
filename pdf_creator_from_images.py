import glob
import os

from PIL import Image


def create_pdf_from_images(directory, output_pdf_name):
    # Change to the directory with images
    os.chdir(directory)

    # Get all image files and sort them
    image_files = glob.glob('*.png') + glob.glob('*.jpg') + glob.glob('*.jpeg')
    image_files.sort()

    # Ensure there are image files
    if not image_files:
        print("No image files found in the directory.")
        return

    # Open the first image to create the pdf
    first_image = Image.open(image_files[0])
    converted_images = []

    # Convert and append other images to the list
    for image_file in image_files[1:]:
        img = Image.open(image_file)
        converted_img = img.convert('RGB')
        converted_images.append(converted_img)

    # Save the images as a PDF
    first_image.convert('RGB').save(
        output_pdf_name, save_all=True, append_images=converted_images)


# Usage example
#create_pdf_from_images('/path/to/your/images', '/path/to/your/output.pdf')

create_pdf_from_images('./images', 'output.pdf')

