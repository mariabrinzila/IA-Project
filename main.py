import data_processing as dp
import classifiers as c
import numpy as np


# Read and process data
dt = dp.Data("train_data.json")
dt.transform_data()
x, y = dt.define_x_y()

# Naive Bayes for identifying the type of sarcasm
classifier = c.BayesClassifier()
classifier.bayes_multinomial(x, y)

# Test on a sentence
user_input = "No I'm not mad at you! I just wanna hit you. In the face. With a chair. Repeatedly."
x_test = dt.process_tweet(user_input)
classifier.prediction(x_test)
