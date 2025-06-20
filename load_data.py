import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("malicious_phish.csv")  # Make sure this is the correct filename

print("🔍 First 5 rows of the dataset:")
print(df.head())

# Step 2: Check dataset shape
print("\n📊 Dataset Size:")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))

# Step 3: Check unique values in 'type'
print("\n🧾 Types of URLs (from 'type' column):")
print(df['type'].value_counts())

# Step 4: Create a binary label column
# 0 = benign (safe)
# 1 = phishing, defacement, malware (all considered malicious)
df['label'] = df['type'].apply(lambda x: 0 if x == 'benign' else 1)

# Step 5: Show new label distribution
print("\n✅ Binary Labels (0 = Safe, 1 = Malicious):")
print(df['label'].value_counts())

# Step 6: Drop unnecessary columns and keep only 'url' and 'label'
df_cleaned = df[['url', 'label']]

# Step 7: Save to new CSV
df_cleaned.to_csv("cleaned_urls.csv", index=False)
print("\n💾 Cleaned dataset saved as 'cleaned_urls.csv'")
