import os
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from numpy import vstack
from matplotlib import pyplot


# plot source, generated and target images
def plot_images(src_img, gen_img, filename):
    images = vstack((src_img, gen_img))
    # scale from [-1,1] to [0,1]
    images = (images + 1) / 2.0
    titles = ['Source', 'Generated']
    # plot images row by row
    for i in range(len(images)):
        # define subplot
        pyplot.subplot(1, 2, 1 + i)
        # turn off axis
        pyplot.axis('off')
        # plot raw pixel data
        pyplot.imshow(images[i])
        # show title
        pyplot.title(titles[i])
    filename = filename.split('.')[0] + '.png'
    pyplot.savefig(output_path + filename)
    print('Saved: ', filename)


# plot just the generated images
def plot_generated_images(gen_image, filename):
    # Scale from [-1,1] to [0,1]
    gen_image = (gen_image + 1) / 2.0
    # Save the generated image
    output_filename = output_path + filename.split('.')[0] + '.png'
    pyplot.imsave(output_filename, gen_image[0])
    print('Saved: ', output_filename)


if __name__ == '__main__':
    test_images_path = ''
    output_path = ''

    model = load_model('50_epochs_3000_images.h5')

    size = (256, 256)

    counter = 0

    for filename in os.listdir(test_images_path):
        # load and resize the image
        img = load_img(test_images_path + filename, target_size=size)
        # convert to numpy array
        src_image = img_to_array(img)
        src_image = np.expand_dims(src_image, axis=0)

        # scale from [0,255] to [-1,1]
        src_image = (src_image - 127.5) / 127.5

        # generate image from source
        gen_image = model.predict(src_image)

        plot_generated_images(gen_image, filename)
        
        counter += 1
        print(counter, 'images predicted!')