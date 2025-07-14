# app.py
from flask import Flask, render_template, request
from extract_features import extract_all
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("model/phishing_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        features = extract_all(url)
        prediction = model.predict([features])[0]
        result = "Phishing 🚨" if prediction == 1 else "Legitimate ✅"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
