import os
import cv2
import numpy as np
# from PIL import Image


def upsample_image(input_image_path, output_image_path):
    '''
    Upsamples the original image to 256x256
    '''

    # Load the 120x120 TIFF image
    input_image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)
    # Resize the image to 256x256 using cubic interpolation for smoother results
    output_image = cv2.resize(input_image, (256, 256),
                              interpolation=cv2.INTER_CUBIC)
    # output_image = output_image[:, :, np.newaxis]
    # Save the resulting image
    cv2.imwrite(output_image_path, output_image)

    print('Upsampled: ', output_image_path)


if __name__ == '__main__':

    input_path = ''
    output_path = ''

    for filename in os.listdir(input_path):
        original_image_path = os.path.join(input_path, filename)
        output_image_path = os.path.join(output_path, filename)

        upsample_image(original_image_path, output_image_path)
