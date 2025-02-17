import pandas as pd 
import numpy as np

df = pd.read_csv('players.csv')

# funcao iloc 
# buscar registros pelo numero do indice 
print(df.iloc[7])  # buscar o setimo registro 


# funcao loc 
# buscar registro por descricao (label) e com booleanos

menores = df.loc[df.Age < 18] # selecionar do dataframe onde o registro em Age seja < 18
print(menores)

# criar dataframes somente com jogadores brasileiros 
brasileiros = df.loc[df.Nation == 'br BRA']
print(brasileiros)

# criar dataframe somente com jogadores do Barcelona
barca = df.loc[df.Squad == 'Barcelona']
print(barca)

# dataframe somente com jogadores do real madrid
madrid = df.loc[df.Squad == 'Real Madrid']
print(madrid)

# fatiamento de registros e colunas 
fatiado = df.iloc[:6, 15:21]
print(fatiado)

