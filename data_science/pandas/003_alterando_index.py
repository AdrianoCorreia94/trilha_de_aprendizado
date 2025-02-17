import pandas as pd 

df = pd.read_csv('players.csv', index_col = 1)  # ler o arquivo e selecionar a coluna 1 como index

jogador = df.loc['Vinicius Júnior']  # utilizar o loc para fazer a busca

print(jogador)