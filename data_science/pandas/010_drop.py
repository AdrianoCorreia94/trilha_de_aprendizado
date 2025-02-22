import pandas as pd 

df = pd.read_csv('players.csv')

df = df.head(10)

print(df)

# excluindo algumas linhas 
new = df.drop([2, 4, 6]) # excluir as linhas 2, 4 e 6

print(new)

# excluir a coluna AvgLen
new = new.drop(['AvgLen'], axis=1)
print(new)

# excluir as colunas Launch%, Opp, Stp%
new = new.drop(['Launch%', 'Opp', 'Stp%'], axis= 1)
print(new)

# excluir linhas
new = new.drop([1], axis=0) # exluindo a linha 1
print(new)