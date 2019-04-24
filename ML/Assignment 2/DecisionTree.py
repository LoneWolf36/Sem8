import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn import tree
import graphviz

#1.reading dataset
data=pd.read_csv("ass2data.csv")
features=data.columns
features=features[1:-1]
class_names=list(set(data.iloc[1:,-1]))
#print(data)

#2.printing the columns which are categorical string types
#for i in data.columns.values:
    #print(data[i].dtypes)

#3.Converting string categorical columns into numerical categorical columns
for i in data.columns.values:
    le=preprocessing.LabelEncoder()
    if data[i].dtypes=="object":
        le.fit(data[i])
        data[i]=le.transform(data[i])
#print(data)

#4.Splitting data into training and testing
X_train=data.values[0:14,1:5]
#print(X_train)
Y_train=data.values[0:14,5]
#print(Y_train)
X_test=data.values[14,1:5]
#print(X_test)

#5.DecisionTree using gini index
# clf_gini=DecisionTreeClassifier(criterion="gini")
# clf_gini.fit(X_train,Y_train)
# output1=clf_gini.predict([X_test])
# print(output1)
# dot_data1=tree.export_graphviz(clf_gini,out_file=None,feature_names=features,class_names=class_names,filled=True,rounded=True,special_characters=True)
# graph=graphviz.Source(dot_data1)
# graph.render('DecisionTreeGini',view=True)

#DecisionTree using entropy and IG
clf_entropy=DecisionTreeClassifier(criterion="entropy")
clf_entropy.fit(X_train,Y_train)
output2=clf_entropy.predict([X_test])
print(output2)

dot_data2=tree.export_graphviz(clf_entropy,out_file=None,feature_names=features,class_names=class_names,filled=True,rounded=True,special_characters=True)
graph=graphviz.Source(dot_data2)
graph.render('DecisionTreeEntropy',view=True)
