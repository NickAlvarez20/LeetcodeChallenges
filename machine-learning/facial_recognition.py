from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import numpy as np

import matplotlib.pyplot as plt


# 1. Load the dataset (This will download about 6mb on first run)
faces = fetch_olivetti_faces()
X = faces.data  # The pixel values (4096 features per image)
y = faces.target  # The ID of the person (0 to 39)

# 2. Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train a Support Vector Machine (SVM)
# SVMs are excellent at finding "boundaries" between diff faces
model = SVC(kernel="linear", probability=True)
model.fit(X_train, y_train)

# 4. Test it on a random "Mystery Face" from the test set
test_index = np.random.randint(0, len(X_test))
mystery_face = X_test[test_index].reshape(1, -1)
true_id = y_test[test_index]

prediction = model.predict(mystery_face)[0]
probs = model.predict_proba(mystery_face)[0]
confidence = np.max(probs) * 100

plt.imshow(faces.images[test_index], cmap="gray")
plt.show()

print(f"Predicted Person ID: {prediction}")
print(f"Actual Person ID: {true_id}")
print(f"Confidence Score: {confidence:.2f}%")
