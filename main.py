
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
import numpy as np
from keras.preprocessing import image
import matplotlib.pyplot as plt
from keras.optimizers import RMSprop

model = Sequential()

# 1 CRP
model.add(Convolution2D(
     filters=32,
     kernel_size=(3,3),
     strides=(1, 1),
     activation='relu',
     input_shape=(150,150,3)
))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

# 2 CRP
model.add(Convolution2D(
     filters=32,
     kernel_size=(3, 3),
     strides=(1, 1),
     activation='relu',
     input_shape=(150, 150, 3)
))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 3 CRP
model.add(Convolution2D(
     filters=32,
     kernel_size=(3, 3),
     strides=(1, 1),
     activation='relu',
     input_shape=(150, 150, 3)
))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 4 CRP
model.add(Convolution2D(
     filters=32,
     kernel_size=(3, 3),
     strides=(1, 1),
     activation='relu',
     input_shape=(150, 150, 3)
))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten Layer
model.add(Flatten())

# 1 Hidden Layer\n",

model.add(Dense(
     units=1024,
     input_shape=(7,),
     activation='relu'
))

# 2 Hidden Layer\n",

model.add(Dense(
     units=720,
     input_shape=(7,),
     activation='relu'
))

# 3 Hidden Layer\n",

model.add(Dense(
     units=600,
     input_shape=(7,),
     activation='relu'
))

# 4 Hidden Layer\n",

model.add(Dense(
     units=712,
     input_shape=(7,),
     activation='relu'
))

# 5 Hidden Layer\n",

model.add(Dense(
     units=600,
     input_shape=(7,),
     activation='relu'
))

# 6 Hidden Layer\n",

model.add(Dense(
     units=512,
     input_shape=(7,),
     activation='relu'
))
# Output Layer\n",

model.add(Dense(
     units=7,
     activation='softmax'
))

# For collecting images from the directory,

train = image.ImageDataGenerator(rescale=1./255,
     rotation_range=45,
     width_shift_range=0.3,
     height_shift_range=0.3,
     horizontal_flip=True,
     fill_mode='nearest')

test = image.ImageDataGenerator(rescale=1./255)

image_test = train.flow_from_directory('D://photos//family_dataset//test',
     target_size=(150, 150),
     class_mode='categorical')


image_train = train.flow_from_directory('D://photos//family_dataset//train',
    target_size=(150, 150),
    class_mode='categorical')

model.compile(loss = 'categorical_crossentropy',
    optimizer = RMSprop(lr = 0.001),
    metrics = ['accuracy'])

history = model.fit_generator(
    generator=image_train,
    epochs = 5,
    validation_data = image_test,
        )

model.summary()
model.save('family.h5')
