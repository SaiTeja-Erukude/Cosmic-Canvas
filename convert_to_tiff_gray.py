from PIL import Image
import os

def convert_to_tiff_gray(input_dir, output_dir):
    '''
    Given an input and output directory, it converts all RGB jpg files to grayscale tiffs
    '''

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all .jpg files in the input directory
    jpg_files = [f for f in os.listdir(input_dir) if f.endswith('.jpg')]

    for jpg_file in jpg_files:

        # Construct the paths for input and output
        input_path = os.path.join(input_dir, jpg_file)
        output_path = os.path.join(output_dir, f"{jpg_file[:-4]}.tiff")

        # Open the .jpg, convert to grayscale and save it as .tiff
        try:
            with Image.open(input_path) as img:
                # Convert to grayscale
                grayscale_img = img.convert('L')
                grayscale_img.save(output_path, format='TIFF')

            print('Converted ', jpg_file)
        except Exception as e:
            print('Error converting ', jpg_file, e)

if __name__ == '__main__':

    input_dir = ''
    output_dir = ''

    convert_to_tiff_gray(input_dir, output_dir)