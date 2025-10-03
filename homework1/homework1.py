# %%
from collections import defaultdict
from sklearn import linear_model
import numpy
import math
import pandas

# %%
### Question 1

# %%
def getMaxLen(dataset):
    # Find the longest review (number of characters)
    df = pandas.read_json(dataset)
    reviews = df['review_text'].tolist()
    maxLen = max(len(s) for s in reviews)
    return maxLen

# %%
def featureQ1(datum, maxLen):
    # Feature vector for one data point
    datum = 0

# %%
def Q1(dataset):
    # Implement...
    return theta, MSE

# %%
### Question 2

# %%
def featureQ2(datum, maxLen):
    # Implement (should be 1, length feature, day feature, month feature)
    return 0

# %%
def Q2(dataset):
    # Implement (note MSE should be a *number*, not e.g. an array of length 1)
    return X2, Y2, MSE2

# %%
### Question 3

# %%
def featureQ3(datum, maxLen):
    # Implement
    return 0

# %%
def Q3(dataset):
    # Implement
    return X3, Y3, MSE3

# %%
### Question 4

# %%
def Q4(dataset):
    # Implement
    return test_mse2, test_mse3

# %%
### Question 5

# %%
def featureQ5(datum):
    # Implement
    return 0

# %%
def Q5(dataset, feat_func):
    # Implement
    return TP, TN, FP, FN, BER

# %%
### Question 6

# %%
def Q6(dataset):
    # Implement
    return precs

# %%
### Question 7

# %%
def featureQ7(datum):
    # Implement (any feature vector which improves performance over Q5)
    return 0

# %%



