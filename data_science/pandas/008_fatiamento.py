'''
    o fatiamento dá pelo indice, sendo o aberto à direita, ou seja, o ultimo indice nao faz parte
'''

import pandas as pd 

df = pd.read_csv('players.csv')


# fatiamento 
print(df[3:17]) # imprimirá o fatiamento do indice 3 ao 16

print(df[-5:])  # imprimir os utimos 5 indices

# ------------------------------------------------------------

# fatiando as colunas
# para fatiar as colunas, usa-se o iloc


print(df.iloc[:, 4:8]) # fatiando todos os registros e colunas 4 a 7 


