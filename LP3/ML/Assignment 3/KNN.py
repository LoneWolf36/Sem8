import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset.csv")
x = data.iloc[:,:-1].values
y = data.iloc[:, 2].values

x_train = x[0:6]
y_train = y[:6]

x_test = x[6]

print(x_train)
print(x_test)

#x_train = np.reshape(x_train,(-1,1))
#y_train = np.reshape(y_train,(-1,1))

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train,y_train)
x_test = np.reshape(x_test,(1,-1))

prediction = classifier.predict(x_test)
print(prediction)
