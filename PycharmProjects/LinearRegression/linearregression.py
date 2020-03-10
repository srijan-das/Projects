import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")

decider = {'yes' : 1, 'no' : 2}
data.romantic = [decider[item] for item in data.romantic]

data = data[["G1", "G2", "G3", "studytime", "failures", "absences", "famrel", "romantic"]]

predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

'''best = 0
for _ in range(50) :
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    if acc > best :
        best = acc
        with open("gradepredictor.pickle", "wb") as f:
            pickle.dump(linear, f)

print (best)'''

model_saved = open("gradepredictor.pickle", "rb")
linear = pickle.load(model_saved)

'print(linear.score(x_test, y_test))'
print("Co :", linear.coef_)
print("\nIntercept : ", linear.intercept_, "\n")

predictions = linear.predict(x_test)

for i in range(len(predictions)) :
    print(predictions[i], x_test[i], y_test[i])

p = 'romantic'
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
