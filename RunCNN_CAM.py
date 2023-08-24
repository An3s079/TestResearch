import cv2
import tensorflow as tf
from keras import Model
import numpy as np

model = tf.keras.models.load_model('CNN.model')
vid = cv2.VideoCapture(1)

class_names = ['Contains Cone', 'No Cone']    



while True:
    ret, frame = vid.read()

    # this is the most disgusting code I have ever written
    cv2.imwrite("brug.jpg", frame)
    img = cv2.imread('brug.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
    x,y,w,h = cv2.boundingRect(thresh)
    crop = img[y:y+h,x:x+w]
    cv2.imwrite('bruh.jpg',crop)
    img2= tf.keras.utils.load_img(
    'bruh.jpg', target_size=(180, 180))
    img_array = tf.keras.utils.img_to_array(img2)
    img_array = tf.expand_dims(img_array, 0) # Create a batch


    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    cv2.imshow("the_cone_zone", frame)
    cv2.setWindowTitle("the_cone_zone","{} ({:.2f}%)".format(class_names[np.argmax(score)], 100 * np.max(score)))

    if cv2.waitKey(4) & 0xFF == ord('q'):
        break

vid.release()

