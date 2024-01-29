import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define your data directories and other parameters
data_dir = '../data/train/'
img_height, img_width = 256, 256
batch_size = 32
epochs = 20

# Load ResNet50 model
base_model = ResNet50(include_top=False, weights='imagenet', input_shape=(img_height, img_width, 3), pooling='avg')

# Freeze the layers of the base model
for layer in base_model.layers:
    layer.trainable = False

# Create a custom model on top of ResNet50
model = models.Sequential([
    base_model,
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Create data generators
train_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

# Save the model architecture to a JSON file
model_name = f'{epochs}_epochs_resnet'
model_json = model.to_json()
with open(f'{model_name}.json', 'w') as json_file:
    json_file.write(model_json)

# Train the model
model.fit(train_generator, epochs=epochs, validation_data=train_generator)

# Save the model weights
model.save_weights(f'{model_name}.h5')