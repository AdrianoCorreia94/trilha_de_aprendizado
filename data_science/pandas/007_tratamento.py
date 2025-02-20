# tratando valores nulos 

import pandas as pd 

df = pd.read_csv('players.csv')

t1 = df.fillna(0)  # troca os valores Nan por 0
t2 = df.fillna('vazio')  # também é possivel trocar por string

print(df)   # df original
print(t1)   # df com troca de NaN por 0
print(t2)   # df com troca de NaN pela string 'vazio'

# visualizar os valores Nan 
teste = df.isna()   # retorna true or false para verificar se é null

print(teste)