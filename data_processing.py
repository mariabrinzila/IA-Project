import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


class Data:
    def __init__(self, json_file):
        self.data = pd.read_json(json_file)
        self.data_to_array = []

    def transform_data(self):
        count_vec = CountVectorizer()
        self.data_to_array = count_vec.fit_transform(self.data["tweet"])
        self.data_to_array = np.array(self.data_to_array.todense())

    def define_x_y(self):
        x = self.data_to_array
        y = self.data["sarcastic"]
        return x, y
