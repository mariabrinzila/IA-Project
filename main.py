import data_processing as dp
import classifiers as c
import graphic_interface as ui


# Read and process data
dt = dp.Data("train_data.json")
dt.transform_data()
x, y, x1, y1 = dt.define_x_y()
print(x.shape)
print(y.shape)
print(x1.shape)
print(y1.shape)

# Naive Bayes for identifying the if the data is sarcastic or not
classifier = c.NearestNeighbours()
classifier.knn(x1, y1)

# Naive Bayes for identifying the type of sarcasm
classifier = c.BayesClassifier()
classifier.bayes_multinomial(x, y)

# Graphic interface, get input from user and generate output
ui.GraphicInterface()
