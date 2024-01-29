import os
import numpy as np
from libtiff import TIFF


def concatenate_images(image1_path, image2_path, output_path):
    '''
    Given two images paths, this function concatenates the image1 with image2 (side by side)
    and stores the resultant Concatenated image in the output_path.
    '''

    # Open the first image
    tif1 = TIFF.open(image1_path, mode='r')
    image1 = tif1.read_image()

    # Open the second image
    tif2 = TIFF.open(image2_path, mode='r')
    image2 = tif2.read_image()

    # Check if images have the same height
    if image1.shape[0] != image2.shape[0]:
        print("Images have different heights. Cannot create collage.")
        return

    # Concatenate the images horizontally
    collage = np.concatenate((image1, image2), axis=1)

    # Save the collage as a new TIFF file
    tif_out = TIFF.open(output_path, mode='w')
    tif_out.write_image(collage)

    print('Concatenated: ', output_path)

    # Close the TIFF files
    tif1.close()
    tif2.close()
    tif_out.close()


if __name__ == '__main__':

    original_images = ''
    annotated_images = ''
    output_path = ''

    # print(len(os.listdir(original_images)))

    for filename in os.listdir(original_images):
        original_image_path = os.path.join(original_images, filename)
        annotated_image_path = os.path.join(annotated_images, filename)
        output_image_path = os.path.join(output_path, filename)

        concatenate_images(original_image_path,
                           annotated_image_path, output_image_path)
