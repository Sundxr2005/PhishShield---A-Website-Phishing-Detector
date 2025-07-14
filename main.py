# main.py
from extract_features import extract_all
import joblib

# Load the trained model
model = joblib.load("model/phishing_model.pkl")

def check_url(url):
    features = extract_all(url)
    prediction = model.predict([features])
    return "Phishing 🚨" if prediction[0] == 1 else "Legitimate ✅"

if __name__ == "__main__":
    while True:
        url = input("\nEnter a URL to check (or type 'exit'): ")
        if url.lower() == 'exit':
            break
        result = check_url(url)
        print(f"🔍 Result: {result}")
