print("Welcome to Malacious Url Detector")

suspicious_keywords = ["login", "verify", "update", "secure", "freegift"]

urls = [
    "https://www.google.com",
    "http://192.168.1.1/login.php",
    "https://secure-bank-update.com/verify",
    "http://freegift.amazon-login.com"
]

for url in urls:
    is_suspicious = any(word in url.lower for word in suspicious_keywords)
    print(f"{url} --> URL Length: {len(url)} --> Suspicious: {is_suspicious}")