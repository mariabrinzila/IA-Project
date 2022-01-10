from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np


class BayesClassifier:
    def __init__(self):
        self.model = MultinomialNB()

    def bayes_multinomial(self, x, y):
        # Compute training data and test data
        # 20% test data, 80% training data
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=8)

        # Create and fit model
        # Maximum accuracy <=> alpha = 0.3
        self.model = MultinomialNB(alpha=0.3).fit(x_train, y_train)

        # Evaluate model
        y_predicted = self.model.predict(x_test)
        print("Accuracy for the Multinomial Naive Bayes is: ", accuracy_score(y_test, y_predicted))

        # Make prediction
        self.prediction(x_test[:10])

    def prediction(self, x_test):
        y_predicted = self.model.predict(x_test)
        print(y_predicted)


class NearestNeighbours:
    def __init__(self):
        self.model = KNeighborsClassifier()

    def knn(self, x, y):
        # Compute training data and test data
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # Create and fit model
        self.model = KNeighborsClassifier().fit(x_train, y_train)

        # Evaluate model
        y_predicted = self.model.predict(x_test)
        print("Accuracy for the K Nearest Neighbours Algorithm: ", accuracy_score(y_test, y_predicted))

        # Make prediction
        self.prediction(x_test[:10])

    def prediction(self, x_test):
        y_predicted = self.model.predict(x_test)
        print(y_predicted)


def bayes_gaussian(x, y):
    # Compute training data and test data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y)

    # Create and fit model
    model = GaussianNB().fit(x_train, y_train)

    # Evaluate model
    y_predicted = model.predict(x_test)
    print("Accuracy for the Gaussian Naive Bayes is: ", accuracy_score(y_test, y_predicted))


def knn(x, y):
    # Compute training data and test data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y)

    # Create and fit model
    model = KNeighborsClassifier().fit(x_train, y_train)

    # Evaluate model
    y_predicted = model.predict(x_test)
    print("Accuracy for the K Nearest Neighbours Algorithm: ", accuracy_score(y_test, y_predicted))

    y_predicted = model.predict(x_test[:10])
    print(y_predicted)


def bayes_bernoulli(json_file):
    # Read data from json file
    data = pd.read_json(json_file)
    data = data[["tweet", "sarcastic"]]

    # Transform data to numpy array
    x = np.array(data["tweet"])
    y = np.array(data["sarcastic"])
    cv = CountVectorizer()
    x = cv.fit_transform(x)

    # Compute training data and test data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Create and fit model
    model = BernoulliNB()
    model.fit(x_train, y_train)

    # Evaluate model
    y_predicted = model.predict(x_test)
    print("Accuracy for the Multinomial Bernoulli Bayes is: ", accuracy_score(y_test, y_predicted))

    # Make a prediction using the model
    user = "Today my pop-pop told me I was not “forced” to go to college 🙃 okay sure sureeee"
    data = cv.transform([user]).toarray()
    output = model.predict(data)

    if output == 0:
        print("Not sarcastic.")
    else:
        print("Sarcastic.")

