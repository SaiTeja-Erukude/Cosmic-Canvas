import os
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import model_from_json

# Load the model architecture from JSON file
with open('20_epochs_resnet.json', 'r') as json_file:
    loaded_model_json = json_file.read()

loaded_model = model_from_json(loaded_model_json)

# Load the model weights
loaded_model.load_weights('20_epochs_resnet.h5')

# Compile the loaded model
loaded_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print('Model Compiled!')

# Provide the path to the image you want to predict
data_dir = '/home/l/lshamir/temp20/ccw/'
output_dir = '/home/e/erukude/cosmic_canvas/resnet50/data/ccw/'

counter = 0
copied = 0

for filename in os.listdir(data_dir):
    img_path = os.path.join(data_dir, filename)

    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image

    # Make predictions
    predictions = loaded_model.predict(img_array)

    contains_arms = False
    if predictions[0] > 0.5:
        contains_arms = True
    
    # Print the result
    print('Contains Arms? ', contains_arms, predictions)

    counter += 1
    print(counter, ' images predicted!')

    # Copy the image if it contains arms
    if contains_arms:
        output_img_path = os.path.join(output_dir, filename)
        with Image.open(img_path) as img:
            img.save(output_img_path)
            copied += 1
            print(copied, ' images copied!')
