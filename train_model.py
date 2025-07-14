# train_model.py
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from extract_features import extract_all

# Load raw dataset
raw_data = pd.read_csv("dataset/phishing_websites.csv")

# Extract 15 new features from the actual URLs
# But UCI dataset doesn’t give raw URLs — so here’s the trick:
# For demo: simulate URLs with extracted feature logic using random samples

# ⚠️ Instead: manually create a new CSV with real URLs
urls = [
    "http://paypal.secure-login.ru", "https://google.com",
    "http://192.168.0.1/login", "https://verify-facebook-update.com",
    "http://apple-login.co", "https://amazon.com"
]
labels = [1, 0, 1, 1, 1, 0]

X = [extract_all(url) for url in urls]
y = labels

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model/phishing_model.pkl")

# Evaluate
pred = model.predict(X_test)
print(classification_report(y_test, pred))
