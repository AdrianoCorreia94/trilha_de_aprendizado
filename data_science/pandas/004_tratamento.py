# tratando valores nulos 

import pandas as pd 

df = pd.read_csv('players.csv')

t1 = df.fillna(0)  # troca os valores Nan por 0
t2 = df.fillna('vazio')  # também é possivel trocar por string

print(df)
print(t1)
print(t2)