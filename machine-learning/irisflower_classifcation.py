from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# load the built in dataset
iris = load_iris()

X, y = iris.data, iris.target

# split into training(80%) and testing (20%) sets
# this allows us to "hide" some data to test the model later
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. init and train the model
# n_neighbors = 3 means it looks at the 3 closest flowers to decide
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Define a mystery flower [sepal length, sepal width, petal length, petal width]
# change these numbers
mystery_flower = np.array([[6.0, 2.5, 0.9, 5.2]])

# 2. Get the specific prediction AND the probabilities
prediction_index = model.predict(mystery_flower)
probabilities = model.predict_proba(mystery_flower)[
    0
]  # Get the first (and only) result

# 3. Format the results
species_name = iris.target_names[prediction_index][0]
confidence = np.max(probabilities) * 100

print(f"Prediction: {species_name.upper()}")
print(f"Confidence: {confidence:.2f}%")

# 4. Show the full breakdown
print("\n--- Probability Breakdown ---")
for i, name in enumerate(iris.target_names):
    print(f"{name.capitalize()}: {probabilities[i]*100:.1f}%")

# # 4. Use the trained model to guess the species
# prediction_index = model.predict(mystery_flower)
# species_name = iris.target_names[prediction_index][0]

# print(f"I've analyzed the measurements: {mystery_flower[0]}")
# print(f"The model identifies this flower as: {species_name.upper()}")

# --- QUICK TEST GUIDE (Approximate Ranges) ---
# SETOSA:     [5.0, 3.4, 1.5, 0.2]  (Small petals)
# VERSICOLOR: [5.9, 2.7, 4.2, 1.3]  (Medium petals)
# VIRGINICA:  [6.5, 3.0, 5.5, 2.0]  (Large petals)
# ----------------------------------------------


# 4. Make predictions and check accuracy
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {score * 100:.2f}%")
print(f"Predicted species for first 5 test flowers: {predictions[:5]}")
print(f"Actual species for first 5 test flowers: {y_test[:5]}")
