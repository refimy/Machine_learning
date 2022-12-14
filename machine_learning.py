# -*- coding: utf-8 -*-
"""machine learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oQAW_RMcuxQymyzNf7nCswbtahRdFmU-
"""

from sklearn import tree

# Database: Gerbang logika AND
# x = Data, Y = Target
x = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2], [2, 3], [3, 2], [3, 3]]
y = [0, 0, 0, 1, 2, 2, 1, 3, 2, 3]

# Training and Classify
clf = tree.DecisionTreeClassifier() 
clf = clf. fit(x, y) 

# Prediksi
print ("Logika AND Metode Desicion Tree") 
print ("0 0 = ", clf.predict([[0, 0]])) 
print ("0 1 = ", clf.predict([[0, 1]])) 
print ("1 0 = ", clf.predict([[1, 0]])) 
print ("1 1 = ", clf.predict([[1, 1]]))
print ("1 2 = ", clf.predict([[1, 2]]))
print ("2 1 = ", clf.predict([[2, 1]]))
print ("2 2 = ", clf.predict([[2, 2]]))
print ("2 3 = ", clf.predict([[2, 3]]))
print ("3 2 = ", clf.predict([[3, 2]]))
print ("3 3 = ", clf.predict([[3, 3]]))