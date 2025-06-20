import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Step 1: Load the dataset
df = pd.read_csv("features.csv")

# Step 2: Features and label
X = df.drop("label", axis=1)
y = df["label"]

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔧 Step 4: Train a smaller Random Forest model
model = RandomForestClassifier(
    n_estimators=10,       # only 10 trees (default is 100)
    max_depth=10,          # limit tree depth (controls model size)
    random_state=42
)
model.fit(X_train, y_train)

# Step 5: Test it
y_pred = model.predict(X_test)
print(f"✅ Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred))
print("\n🧾 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 6: Save the model
joblib.dump(model, "malicious_url_model.pkl")
print("\n💾 Model saved as 'malicious_url_model.pkl'")
