import glob
import os
import shutil

# Note: Remeber to create a backup of the images, because the script rename the images irreversibly
def rename_images_sorted():
    # Get all .png files in the current directory and sort them
    png_files = glob.glob('*.png')
    png_files.sort()

    # Iterate over the sorted files and rename them
    for index, file in enumerate(png_files):
        # Create the new filename with leading zeros
        new_filename = f"{str(index).zfill(3)}.png"

        # Rename the file
        shutil.move(file, new_filename)


# Call the function
rename_images_sorted()
