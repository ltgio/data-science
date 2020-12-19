# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:42:10 2019

@author: giann
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy  as np
import os

from sklearn.preprocessing   import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble        import RandomForestClassifier
from sklearn.metrics         import accuracy_score
from pathlib                 import Path

# set root directory
path_root = Path("C:/Users/giann/data-science-core")
os.chdir(path_root)
print(f'- Root directory = {os.getcwd()}')

# load data
path_dataset = path_root / 'dataset/credit.csv'
data      = pd.read_csv(path_dataset) 
data.head()

# Feature engineering
# Comparison between OneHotEncoder and LabelEncoder

# Create numeric encoding for credit_history
credit_history_num = LabelEncoder().fit_transform(data['credit_history'])

# Create a new feature matrix including the numeric encoding
X_num = pd.concat([X, pd.Series(credit_history_num)], 1)

# Create new feature matrix with dummies for credit_history
X_hot = pd.concat([X, pd.get_dummies(credit['credit_history'])], 1)

# Compare the number of features of the resulting DataFrames
X_hot.shape[1] > X_num.shape[1]


#Feature transformations
#You are discussing the credit dataset with the bank manager. She suggests that the 
# safest loan applications tend to request mid-range credit amounts. Values that are 
# either too low or too high suggest high risk. This means that a non-linear relationship 
# might exist between this variable and the class. You want to test this hypothesis. You will 
# construct a non-linear transformation of the feature. Then, you will compare its association with the class to the original feature. You will use the f_classif scoring function from the last lesson to measure association strength.
#The data is available as a pandas DataFrame called credit, with the class contained in the column class. You have preloaded f_classif, pandas as pd and numpy as np.

# Function computing absolute difference from column mean
def abs_diff(x):
    return np.abs(x-np.mean(x))

# Apply it to the credit amount and store to new column
credit['credit_amount_diff'] = abs_diff(credit['credit_amount'])

# Score old and new versions of this feature with f_classif()
scores = f_classif(credit[['credit_amount', 'credit_amount_diff']], credit['class'])[0]

# Inspect the scores and drop the lowest-scoring feature
credit_new = credit.drop(['credit_amount'], 1)





#You just joined an arrhythmia detection startup and want to train a model on the arrhythmias dataset. You noticed that random forests tend to win quite a few Kaggle competitions, so you want to try that out with a maximum depth of 2, 5, or 10, using grid search. You also observe that the dimension of the dataset is quite high so you wish to consider the effect of a feature selection method.

#To make sure you don't overfit by mistake, you have already split your data. You will use X_train and y_train for the grid search, and X_test and y_test to decide if feature selection helps. All four dataset folds are preloaded in your environment. You also have access to GridSearchCV(), train_test_split(), SelectKBest(), f_classif() and RandomForestClassifier as rfc.


# Find the best value for max_depth among values 2, 5 and 10
grid_search = GridSearchCV(RandomForestClassifier(random_state=1), param_grid={'max_depth': [2, 5, 10]})
best_value = grid_search.fit(X_train, y_train).best_params_['max_depth']

# Using the best value from above, fit a random forest
clf = RandomForestClassifier(random_state=1, max_depth=best_value).fit(X_train, y_train)

# Apply SelectKBest with f_classif and pick top 100 features
vt = SelectKBest(f_classif, k=100).fit(X_train, y_train)

# Refit the classifier using best_depth on the reduced data
clf_vt = RandomForestClassifier(random_state=1, max_depth=best_value).fit(vt.transform(X_train), y_train)

# You are already able to handle hundreds of features in a few lines of code! But what if the optimal number of estimators is different if you first apply feature selection? In Chapter 3 you will learn how to put your pipelines on steroids so that such questions can be asked in just one line of code.