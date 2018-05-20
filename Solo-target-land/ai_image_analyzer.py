#!/usr/bin/env python2

from keras.models import load_model
from keras.optimizers import Adam
from keras.preprocessing import image
import numpy as np

Model = "../target_detection3.h5"

class ai_image_analyzer:

    def __init__(self):
        self.model = load_model(Model)
        self.model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['accuracy'])

    def isTarget(self, path):
        test_image = image.load_img(path, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = self.model.predict(test_image)
       
        is_target = np.argmax(result[0]) == 1
        print("Test")
        print(result)

        
        return is_target
        