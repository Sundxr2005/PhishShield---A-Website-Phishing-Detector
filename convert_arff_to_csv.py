# convert_arff_to_csv.py
import arff
import pandas as pd

with open("Training Dataset.arff", 'r') as f:
    dataset = arff.load(f)

df = pd.DataFrame(dataset['data'], columns=[attr[0] for attr in dataset['attributes']])
df.to_csv("dataset/phishing_websites.csv", index=False)
print("✅ ARFF file converted to CSV!")
