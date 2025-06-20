import streamlit as st
import joblib
import re

# Step 1: Load the trained model
model = joblib.load("malicious_url_model.pkl")

# Step 2: Define suspicious keywords
suspicious_keywords = ['login', 'verify', 'update', 'free', 'bonus', 'secure', 'account']

# Step 3: Feature extraction from a single URL
def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['has_https'] = 1 if url.startswith("https") else 0
    ip_pattern = r'http[s]?://(?:\d{1,3}\.){3}\d{1,3}'
    features['has_ip'] = 1 if re.match(ip_pattern, url) else 0
    features['has_suspicious_keyword'] = 1 if any(word in url.lower() for word in suspicious_keywords) else 0
    return [list(features.values())]  # return as list of list for prediction

# Step 4: Streamlit UI
st.title("🔍 Malicious URL Detector")
st.write("Enter a URL and check if it’s safe or malicious.")

# Input box
user_input = st.text_input("Enter URL")

if st.button("Check"):
    if user_input:
        input_features = extract_features(user_input)
        prediction = model.predict(input_features)[0]

        if prediction == 1:
            st.error("⚠️ This URL is MALICIOUS!")
        else:
            st.success("✅ This URL is SAFE.")
    else:
        st.warning("Please enter a URL.")
