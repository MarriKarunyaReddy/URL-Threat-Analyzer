import pandas as pd
import re
from urllib.parse import urlparse

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_urls.csv")

# Step 2: Define suspicious keywords
suspicious_keywords = ['login', 'verify', 'update', 'free', 'bonus', 'secure', 'account']

# Step 3: Function to extract features from a single URL
def extract_features(url):
    features = {}

    # Basic features
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['has_https'] = 1 if url.startswith("https") else 0

    # IP address instead of domain name
    ip_pattern = r'http[s]?://(?:\d{1,3}\.){3}\d{1,3}'
    features['has_ip'] = 1 if re.match(ip_pattern, url) else 0

    # Suspicious keyword presence
    features['has_suspicious_keyword'] = 1 if any(word in url.lower() for word in suspicious_keywords) else 0

    return features

# Step 4: Apply feature extraction to all URLs
feature_list = df['url'].apply(extract_features)
features_df = pd.DataFrame(feature_list.tolist())

# Step 5: Combine features with labels
final_df = pd.concat([features_df, df['label']], axis=1)

# Step 6: Save to CSV
final_df.to_csv("features.csv", index=False)

print("✅ Feature extraction complete. Saved as 'features.csv'")
print("\n📊 Preview of features:")
print(final_df.head())
