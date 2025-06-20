import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Step 1: Load the feature dataset
df = pd.read_csv("features.csv")

# Step 2: Separate inputs (X) and output (y)
X = df.drop("label", axis=1)  # All columns except label
y = df["label"]               # The label column (0 or 1)

# Step 3: Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Predict on test data
y_pred = model.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy:.2f}")

print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred))

print("\n🧾 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 7: Save the model to a file
joblib.dump(model, "malicious_url_model.pkl")
print("\n💾 Model saved as 'malicious_url_model.pkl'")
