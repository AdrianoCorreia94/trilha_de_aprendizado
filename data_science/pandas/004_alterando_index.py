import pandas as pd 

# carregar o arquivo players.csv como um dataframe e alterar a coluna que será o indice 
df = pd.read_csv('players.csv', index_col = 1)

print(df)