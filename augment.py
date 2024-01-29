import os
import cv2
import tifffile as tiff
from scipy.ndimage import rotate


def augment_img(img_path, result_folder_path):
    # augments the img and stores it in the result folder

    if not os.path.exists(img_path):
        return

    image = tiff.imread(img_path)
    filename = img_path.split('\\')[-1].split('.')[0]

    # Flip the image horizontally
    flipped_horizontal = cv2.flip(image, 1)

    # Flip the image vertically
    flipped_vertical = cv2.flip(image, 0)

    # Rotate the image by 45 degrees
    rotated_90 = rotate(image, 90, reshape=False)

    tiff.imsave(os.path.join(result_folder_path, filename +
                '_horizontal.tif'), flipped_horizontal)
    tiff.imsave(os.path.join(result_folder_path, filename +
                '_vertical.tif'), flipped_vertical)
    tiff.imsave(os.path.join(result_folder_path, filename +
                '_rotated90.tif'), rotated_90)
    tiff.imsave(os.path.join(result_folder_path, filename + '.tif'), image)

    print('Augmented: ', filename)


if __name__ == '__main__':

    galaxies_path = ''
    annotated_path = ''

    aug_galaxies_path = ''
    aug_annotated_path = ''

    for filename in os.listdir(annotated_path):
        galaxy_img_path = os.path.join(galaxies_path, filename)
        annotated_img_path = os.path.join(annotated_path, filename)
        augment_img(galaxy_img_path, aug_galaxies_path)
        augment_img(annotated_img_path, aug_annotated_path)
