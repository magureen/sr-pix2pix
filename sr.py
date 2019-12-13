import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img
import numpy as np
import os
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='*')
parser.add_argument('--model', default='./model/generator.h5')
args = parser.parse_args()

generator = tf.keras.models.load_model(args.model)

for path in args.files:
    img = load_img(path)
    img = np.array([img_to_array(img) / 127.5 - 1])

    print('convert {}'.format(path))
    start_time = datetime.datetime.now()
    results = generator.predict(img)
    elapsed_time = datetime.datetime.now() - start_time

    img = array_to_img((results[0] + 1) * 127.5)
    output_path = os.path.splitext(path)[0] + '-sr.png'
    img.save(output_path)
    print('saved {} Time:{}'.format(output_path, elapsed_time))

