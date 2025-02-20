import pandas as pd 


dataframe = pd.read_csv('players.csv', index_col = 5)

print(dataframe.loc[dataframe.Age < 18])