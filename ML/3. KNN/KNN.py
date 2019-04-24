import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

dataset = pd.read_csv("dataset.csv", sep=',')
print(dataset.head())
le = preprocessing.LabelEncoder()

feature1 = dataset.iloc[:, 0]
feature2 = dataset.iloc[:, 1]
Y = dataset.iloc[:, 2]

# feature1_encoded = le.fit_transform(feature1)
# feature2_encoded = le.fit_transform(feature2)
Y_encoded = le.fit_transform(Y)
print(Y_encoded)

# print(feature1_encoded)
# print(feature2_encoded)

features = list(zip(feature1, feature2))

model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training sets
model.fit(features, Y_encoded)

# Predict Output
predicted = model.predict([[163, 61]]) 
print(predicted)

"""
KNN performs better with a lower number of features than a large number of features. You can say that when the number of features increases than it requires more data. Increase in dimension also leads to the problem of overfitting. To avoid overfitting, the needed data will need to grow exponentially as you increase the number of dimensions. This problem of higher dimension is known as the Curse of Dimensionality.
"""
