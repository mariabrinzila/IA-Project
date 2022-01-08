import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def data_processing():
    # Read the data
    data = pd.read_json('train_data.json')
    tweets = data["tweet"]
    sarcastic = data["sarcastic"]
    print(tweets)
    return tweets, sarcastic


def classify(tweets, sarcastic):
    train, test, train_labels, test_labels = train_test_split(tweets, sarcastic, test_size=0.40, random_state=42)
    gnb = GaussianNB()
    model = gnb.fit(train, train_labels)
    preds = gnb.predict(test)
    print(accuracy_score(test_labels, preds))
