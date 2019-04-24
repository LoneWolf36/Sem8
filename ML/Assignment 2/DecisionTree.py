import os
os.environ["PATH"] += os.pathsep + "D:\Program Files (x86)\Graphviz\Bin"
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import preprocessing
import graphviz

# 1. Reading dataset
data = pd.read_csv("d:\Documents\Sem8\ML\Assignment 2\Ass2data.csv", sep=',')
features = data.columns
features = features[1:-1]
class_names = list(set(data.iloc[1:, -1]))

print("Dataset Length: ", len(data))
print("Dataset Shape: ", data.shape)

print("Dataset: ")
print(data.head())

# # 2. Printing the columns which are categorical string types
# for i in data.columns.values:
#     print(data[i].dtypes)

# 3.Converting string categorical columns into numerical categorical columns
for i in data.columns.values:
    le = preprocessing.LabelEncoder()
    if data[i].dtypes == "object":
        le.fit(data[i])
        data[i] = le.transform(data[i])
print(data)

X = data.values[:, 0:4]
y = data.values[:, 5]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=100)

clf_gini = DecisionTreeClassifier(criterion="gini")
clf_gini.fit(X_train, y_train)

clf_entropy = DecisionTreeClassifier(criterion="entropy")
clf_entropy.fit(X_train, y_train)

y_pred = clf_gini.predict(X_test)
print("Accuracy of decision tree with Gini index is: ",
      accuracy_score(y_test, y_pred)*100)

print("\nPredictions by Gini index: ", y_pred)

y_pred_en = clf_entropy.predict(X_test)
print("Accuracy of decision tree with Entropy is: ",
      accuracy_score(y_test, y_pred_en)*100)

print("\nPredictions by Entropy: ", y_pred_en)

dot_data1 = tree.export_graphviz(clf_gini, out_file=None, feature_names=features,
                                 class_names=class_names, filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data1)
graph.render('DecisionTreeGini', view=True)


dot_data2 = tree.export_graphviz(clf_entropy, out_file=None, feature_names=features,
                                 class_names=class_names, filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data2)
graph.render('DecisionTreeEntropy', view=True)
