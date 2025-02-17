import pandas as pd 

# lendo arquivo csv
df = pd.read_csv('players.csv')

'''
# acessando colunas 

# op1 - acessar como atributo
print(df.Player)
print(df.Age)

# op2 acessar pelo chave 
print(df['Born'])


# mostrar os 6 primeiros registros 
print(df.head(6))  # intervalo fechado 

# mostrar os 6 ultimos registros
print(df.tail(6))  # intervalo fechado 

# ver a quantidade de registros no dataframe
print(len(df))

# ver o tipo de dados de cada campo 
print(df.dtypes)

# estatisticas sobre os dados
print(df.describe())
'''


# fatiamento
print(df[5:12])  # aberto à direita, ultimo indice nao incluso

# acessar os valores numericos
print(df.Age[8:19].values) # retorna uma lista com os valores, util para enviar o dados para modelo de regressao
