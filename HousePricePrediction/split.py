import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_excel("HousePricePrediction.xlsx")

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

X = dataset.drop(['SalePrice'], axis=1)
Y = dataset['SalePrice']

# Split the training set into
# training and validation set
c=X_train, X_valid, Y_train, Y_valid = train_test_split(
	X, Y, train_size=0.8, test_size=0.2, random_state=0)
print(c)

