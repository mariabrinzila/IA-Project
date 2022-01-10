import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


class Data:
    def __init__(self, json_file):
        self.data = pd.read_json(json_file)
        self.data_to_array = []
        self.tweets = []
        self.label = []
        self.corpus = []

    def process_tweet(self, tweet):
        words = tweet
        self.transform_tweet(words)

        tfidf_vec = TfidfVectorizer(max_features=None)
        x_test = tfidf_vec.fit_transform(self.corpus).toarray()
        return x_test

    def transform_data(self):
        self.tweets = self.data.loc[self.data["sarcastic"].astype(int) == 1]
        self.tweets = self.tweets.drop(["sarcastic", "sarcasm", "irony", "satire", "understatement",
                                        "overstatement", "rhetorical_question"], axis=1)

        # Process data: tweets["text"] <=> tweet, rephrase
        self.tweets["text"] = self.tweets["tweet"]

        # For each sarcastic tweet, compute a string with all the categories (example: 010010)
        self.label = self.data.loc[self.data["sarcastic"] == 1]
        self.label["types"] = self.label["sarcasm"].astype(int).astype(str) + \
            self.label["irony"].astype(int).astype(str) + \
            self.label["satire"].astype(int).astype(str) + \
            self.label["understatement"].astype(int).astype(str) + \
            self.label["overstatement"].astype(int).astype(str) + \
            self.label["rhetorical_question"].astype(int).astype(str)

        # Transform text
        words = self.tweets.copy()
        self.transform_text(words)

    def transform_text(self, words):
        lemmatizer = WordNetLemmatizer()
        self.corpus = []
        corpus_test = []

        for i in range(len(words)):
            review = re.sub('[^a-zA-Z]', ' ', words["text"][i])
            review = review.lower()
            review = review.split()
            review = [lemmatizer.lemmatize(word) for word in review
                      if not word in stopwords.words('english')]
            review = ' '.join(review)
            self.corpus.append(review)

    def transform_tweet(self, words):
        lemmatizer = WordNetLemmatizer()
        self.corpus = []
        corpus_test = []

        for i in range(len(words)):
            review = re.sub('[^a-zA-Z]', ' ', words)
            review = review.lower()
            review = review.split()
            review = [lemmatizer.lemmatize(word) for word in review
                      if not word in stopwords.words('english')]
            review = ' '.join(review)
            self.corpus.append(review)

    def define_x_y(self):
        tfidf_vec = TfidfVectorizer(max_features=None)
        x = tfidf_vec.fit_transform(self.corpus).toarray()
        y = self.label["types"]
        print(x.shape)
        return x, y
