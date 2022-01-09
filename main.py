import data_processing as dp
import classifiers as c


# Read and process data
dt = dp.Data("train_data.json")
dt.transform_data()
x, y = dt.define_x_y()

# Use classifiers and print accuracy
c.knn(x, y)
c.bayes_gaussian(x, y)
c.bayes_bernoulli("train_data.json")
c.bayes_multinomial(x, y)
