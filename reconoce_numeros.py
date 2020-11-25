import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist

(training_data, training_labels), (test_data, test_labels) = mnist.load_data()
training_data = training_data / 255
test_data = test_data / 255


model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", 
                 metrics = ['accuracy'])

print("Entrena")
model.fit(training_data, training_labels, epochs=5)

print("Evalua")
model.evaluate(test_data, test_labels)

print("Predice")
predictions = model.predict(test_data)
print(test_labels[0])
print(predictions[0])
