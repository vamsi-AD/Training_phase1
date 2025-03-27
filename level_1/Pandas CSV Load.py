import pandas as pd

data_df = pd.read_csv('datasets/PERSON.csv')

print(data_df.head(5))

print(data_df.describe())