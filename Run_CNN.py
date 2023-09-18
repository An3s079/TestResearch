import tensorflow as tf
import os
import matplotlib.pyplot as plt
import numpy as np
model = tf.keras.models.load_model("Model.CNN")
class_names = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

plt.figure(figsize=(11, 11))
i = 1
for filename in os.listdir("TESTO"):
    ax = plt.subplot(4, 4, i)
    img2= tf.keras.utils.load_img(
     "TESTO\\"+filename, target_size=(288, 432))
    img_array = tf.keras.utils.img_to_array(img2)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    plt.imshow(img2)
    
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    label = filename + ": " + "{} ({:.2f}%)".format(class_names[np.argmax(score)], 100 * np.max(score))
    plt.title(label)
    plt.axis("off")
    i += 1

plt.show()
