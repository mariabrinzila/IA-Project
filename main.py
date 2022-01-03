# TO DO: extract text from a social media post given as a link by the user
# TO DO: create database with training data
import convert_csv_to_json as cj

# cj.csvToJson('train_data.csv', 'training_data.json')

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

data = pd.read_json('Sarcasm.json')

print(data.head())

data["is_sarcastic"] = data["is_sarcastic"].map({0: "Not Sarcasm", 1: "Sarcasm"})
print(data.head())

data = data[["headline", "is_sarcastic"]]
x = np.array(data["headline"])
y = np.array(data["is_sarcastic"])

cv = CountVectorizer()
X = cv.fit_transform(x)  # Fit the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = BernoulliNB()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

user = input("Enter a Text: ")
data = cv.transform([user]).toarray()
output = model.predict(data)
print(output)
