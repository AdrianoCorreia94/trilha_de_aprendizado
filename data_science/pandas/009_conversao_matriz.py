# converter os dados em uma matriz numpy 

import pandas as pd 

df = pd.read_csv('players.csv')

print(df.head(1))

conversao = df.iloc[:16, :8].values     # transforma os registros em uma matriz 

print(conversao)