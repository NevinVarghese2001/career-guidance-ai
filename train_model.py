import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("data/training_data.csv")

X = data.drop("course", axis=1)
y = data["course"]

# Train model
model = DecisionTreeClassifier(
    max_depth=5,
    min_samples_leaf=2,
    random_state=42
)
model.fit(X, y)

# Save model
joblib.dump(model, "career_model.pkl")

print("✅ Career guidance model trained successfully")