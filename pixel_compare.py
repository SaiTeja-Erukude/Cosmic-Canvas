import os
import numpy as np
from libtiff import TIFF


def pixel_to_pixel_compare(skeleton_img_path, galaxy_img_path, result_img_path):
    '''
    Given a skeleton image path and a galaxy image path, 
    this function compares pixel to pixel and creates a new image that is a superimpose of the skeleton on the galaxy image    
    '''

    skeleton_tif = TIFF.open(skeleton_img_path, mode='r')
    width, height = skeleton_tif.GetField(
        'ImageWidth'), skeleton_tif.GetField('ImageLength')

    skeleton_img = skeleton_tif.read_image()

    galaxy_tif = TIFF.open(galaxy_img_path, mode='r')
    galaxy_img = galaxy_tif.read_image()

    # Create a copy of galaxy image
    result_img = np.copy(galaxy_img)

    # if the pixel in skeleton is not black => put a white pixel in the new image
    # else do nothing
    for y in range(height):
        for x in range(width):
            pixel = skeleton_img[y, x]

            # Check if the pixel is not black
            if np.any(pixel != 0):
                result_img[y, x] = 255

    result_img_tif = TIFF.open(result_img_path, mode='w')
    result_img_tif.write_image(result_img)
    result_img_tif.close()

    print('Finished: ', result_img_path)


if __name__ == '__main__':

    skeleton_path = ''
    galaxies_path = ''
    result_path = ''

    for filename in os.listdir(skeleton_path):
        skeleton_img_path = os.path.join(skeleton_path, filename)
        galaxy_img_path = os.path.join(galaxies_path, filename)
        result_img_path = os.path.join(result_path, filename)
        pixel_to_pixel_compare(
            skeleton_img_path, galaxy_img_path, result_img_path)