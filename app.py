import streamlit as st
import gdown
import joblib
import re
import os

# === Setup ===

# Model file setup
MODEL_PATH = "malicious_url_model.pkl"
FILE_ID = "1GmSMUAo_5OfIKlYixjUDTpc7OJ_kWweU"  # ⛔ Replace with your actual Google Drive File ID

# Download the model if not already downloaded
if not os.path.exists(MODEL_PATH):
    st.info("Downloading model from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", MODEL_PATH, quiet=False)

# Load model
model = joblib.load(MODEL_PATH)

# Suspicious keywords to detect
suspicious_keywords = ['login', 'verify', 'update', 'free', 'bonus', 'secure', 'account']

# === Feature extraction function ===
def extract_features(url):
    features = {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'has_https': 1 if url.startswith("https") else 0,
        'has_ip': 1 if re.match(r'http[s]?://(?:\d{1,3}\.){3}\d{1,3}', url) else 0,
        'has_suspicious_keyword': 1 if any(word in url.lower() for word in suspicious_keywords) else 0
    }
    return [list(features.values())]

# === Streamlit UI ===
st.title("🔍 Malicious URL Detector")
st.write("Enter a URL to check if it's safe or potentially malicious.")

# URL input
user_input = st.text_input("Enter a URL:")

# Predict button
if st.button("Check"):
    if user_input:
        features = extract_features(user_input)
        prediction = model.predict(features)[0]
        
        if prediction == 1:
            st.error("⚠️ This URL is MALICIOUS!")
        else:
            st.success("✅ This URL is SAFE.")
    else:
        st.warning("Please enter a URL.")
