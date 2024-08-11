import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("HousePricePrediction.xlsx")

dataset.drop(['Id'],
			axis=1,
			inplace=True)

dataset['SalePrice'] = dataset['SalePrice'].fillna(
dataset['SalePrice'].mean())

new_dataset = dataset.dropna()


new_dataset.isnull().sum()

print(new_dataset)