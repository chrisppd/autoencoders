from tensorflow import keras
from keras import layers

def model1(model): # Autoencoder1 and colorizer1
    # Encoder
    model.add(layers.Conv2D(filters=8, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=12, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))

    # Decoder
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=12, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=3, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    return model
    
def model2(model): # Autoencoder2
    # Encoder
    model.add(layers.Conv2D(filters=8, kernel_size=(5, 5), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(4, 4), padding='same'))
    model.add(layers.Conv2D(filters=12, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(4, 4), padding='same'))
    model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))

    # Decoder
    model.add(layers.UpSampling2D(size=(4, 4)))
    model.add(layers.Conv2D(filters=12, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.UpSampling2D(size=(4, 4)))
    model.add(layers.Conv2D(filters=3, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    return model

def model3(model): # Autoencoder3
    #Encoder
    model.add(layers.Conv2D(filters=8, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=12, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))

    #Decoder
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=12, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=24, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=3, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    return model

def model4(model): # Colorizer2
    # Encoder
    model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=256, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=512, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))

    # Decoder
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=256, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=3, kernel_size=(3, 3), strides=(1, 1), activation='sigmoid', padding='same'))
    return model

def model5(model): # Colorizer3
    # Encoder
    model.add(layers.Conv2D(filters=8, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.AveragePooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.AveragePooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))

    # Decoder
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    model.add(layers.UpSampling2D(size=(2, 2)))
    model.add(layers.Conv2D(filters=3, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
    return model












    
