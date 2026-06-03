from sklearn.tree import DecisionTreeClassifier
import numpy as np

# 1. Prepare Data
# Features [Weight in grams, Texture (1=Smooth, 0=Bumpy)]
X = np.array([[140, 1], [130, 1], [150, 0], [170, 0]])
# Labels [0=Apple, 1=Orange]
y = np.array([0, 0, 1, 1])

# 2. Initialize and Train Model
model = DecisionTreeClassifier()
model.fit(X, y)

# 3. Predict for a new sample (e.g., 145g and Smooth)
test_sample = [[145, 1]]
test_sample_2 = [[40, 0.5]]

prediction = model.predict(test_sample_2)

# Output result
fruit_type = "Apple" if prediction[0] == 0 else "Orange"
print(f"The model predicts this fruit is an: {fruit_type}")
