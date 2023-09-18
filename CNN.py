# code modified from https://www.tensorflow.org/tutorials/load_data/images

import tensorflow as tf
from keras import Model
import matplotlib.pyplot as plt
trainds = tf.keras.utils.image_dataset_from_directory(
    "Data",
    image_size= (288, 432),
    validation_split=0.1,
    subset="training",
    seed=123
    )

valds = tf.keras.utils.image_dataset_from_directory(
    "Data",
    image_size= (288, 432),
    validation_split=0.1,
    subset="validation",
    seed=123
    )
trainds = trainds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
valds = valds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)

model = tf.keras.Sequential([
  tf.keras.layers.Rescaling(1./255),
  tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(288, 432)),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10)
])

model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])
           
history = model.fit(
  trainds,
  validation_data=valds,
  epochs=10
)

#https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/
training_loss = history.history['loss']
test_loss = history.history['val_loss']
val_acc = history.history['val_accuracy']
train_acc = history.history['accuracy']

epoch_count = range(1, len(training_loss) + 1)

plt.plot(epoch_count, training_loss, 'r--')
plt.plot(epoch_count, test_loss, 'b-')
plt.title('Model Loss')
plt.legend(['Training Loss', 'Validation Loss'], loc='upper left')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

plt.plot(epoch_count, train_acc, 'r--')
plt.plot(epoch_count, val_acc, 'b-')
plt.title('Model Accuracy')
plt.legend(['Training Accuracy', 'Validation Accuracy'], loc='upper left')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()
model.save("Model.CNN")