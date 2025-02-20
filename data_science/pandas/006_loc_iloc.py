import pandas as pd 

df = pd.read_csv('players.csv', index_col= 0)


# funcao iloc 
# buscar registros pelo numero do indice 
print(df.head(14))
print(df.iloc[9])  # imprimir o registro da linha 9 (inicio da contagem linha 0)

# --------------------------------------------------------------------------------

# funcao loc 
# buscar registro por descricao (label) e com booleanos

# imprimir registros onde os dados da coluna age sejam menor 18
print(df.loc[df.Age < 18])

'''
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

'''
