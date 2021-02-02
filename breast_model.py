# -*- coding: utf-8 -*-
"""BREAST_MODEL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uDXNIbDBPVq85DBLx5LL1JtwUWiyYbdS
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

data1=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/BreastCancer.csv')

data=data1.copy()
del data['Unnamed: 32']
data=data.iloc[0:, 0:12]


df['diagnosis']= df['diagnosis'].map({'M':1,'B':0})

X=data[['radius_mean', 'perimeter_mean', 'area_mean', 'concave points_mean']]
y=data['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size= 0.3, random_state=1)
rf = RandomForestRegressor(n_estimators = 1000, random_state = 1)
rf.fit(X_train, y_train)

pickle.dump(rf, open('/content/drive/MyDrive/Colab Notebooks/cancer_model.pkl', 'wb'))
save=data.to_csv('bc.csv')