import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Load and Organize Data
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target  # 0 = Malignant, 1 = Benign

# 2. Split into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

# 3. Train the Model
# Logistic Regression is great for binary (Yes/No) classification
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# 4. Evaluate Performance
predictions = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, predictions)*100:.2f}%")
print("\nDetailed Report:")
print(classification_report(y_test, predictions, target_names=data.target_names))

# 5. Generate the Heatmap
# We focus on 'mean' features to prevent the map from getting too crowded
mean_cols = [col for col in df.columns if "mean" in col] + ["target"]
plt.figure(figsize=(12, 8))
sns.heatmap(df[mean_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation: Identifying Cancerous Indicators")
plt.show()
