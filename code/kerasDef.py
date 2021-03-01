from keras.models import Sequential

# mode of model definition
model = Sequential()

from keras.layers import Dense

# add layers
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

# create model
model.compile(loss='categorical_crossentropy',
        optimizer='sgd',
        metrics=['accuracy'])
