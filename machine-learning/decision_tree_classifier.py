import numpy as np

# Data: [Weight, Texture] -> Fruit Type (0: Apple, 1: Orange)
# Texture: 1 = Smooth, 0 = Bumpy
X = np.array([[140, 1], [130, 1], [150, 0], [170, 0]])
y = np.array([0, 0, 1, 1])


def predict_fruit(new_sample, training_features, training_labels):
    # 1. Calculate the distance between the new sample and all training points
    distances = np.sqrt(np.sum((training_features - new_sample) ** 2, axis=1))

    # 2. Find the index of the closest known fruit
    closest_index = np.argmin(distances)

    # 3. Return the label of that closest fruit
    return training_labels[closest_index]


# Prediction for [145, 1]
new_fruit = np.array([145, 1])
result = predict_fruit(new_fruit, X, y)

print(f"Prediction: {'Apple' if result == 0 else 'Orange'}")
# Output: Prediction: Apple
