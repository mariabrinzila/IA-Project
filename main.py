import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import convert_csv_to_json as cj
import classification as cl

<<<<<<< HEAD

def try1():
    # cj.csvToJson('train_data.csv', 'train_data.json')
    data = pd.read_json('train_data.json')
    data = data[["tweet", "sarcastic"]]
    print(data)

    x = np.array(data["tweet"])
    y = np.array(data["sarcastic"])

    cv = CountVectorizer()
    X = cv.fit_transform(x)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    model = BernoulliNB()
    model.fit(X_train, y_train)
    # print(model.score(X_test, y_test))

    user = input("Enter a Text: ")
    data = cv.transform([user]).toarray()
    output = model.predict(data)

    if output == 0:
        print("Not sarcastic.")
    else:
        print("Sarcastic.")


tweets, sarcastic = cl.data_processing()
cl.classify(tweets, sarcastic)

# TO DO: extract text from a social media post given as a link by the user
# TO DO: create database with training data
=======
# cj.csvToJson('train_data.csv', 'train_data.json')
data = pd.read_json('train_data.json')
data = data[["tweet", "sarcastic"]]
print(data)

x = np.array(data["tweet"])
y = np.array(data["sarcastic"])

cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = BernoulliNB()
model.fit(X_train, y_train)
# print(model.score(X_test, y_test))

user = input("Enter a Text: ")
data = cv.transform([user]).toarray()
output = model.predict(data)

if output == 0:
    print("Not sarcastic.")
else:
    print("Sarcastic.")
>>>>>>> ed3f986457c8215b5ee66488b052d01a716751c7
