import pandas as pd 

# criando um dataserie a partir de uma lista
my_list = [12, 23, 34, 45, 56, 67, 78, 89, 90]  # lista com os dados do dataseries
my_series = pd.Series(my_list)  # criando o dataseries a partir da lista

print(my_series)   # exibindo o dataseries
print(f"Format {type(my_series)}")  # imprimido o tipo do objeto my_series 

# --------------------------------------------------------------------------------

# criando a partir de um dicionario
my_dict = {'a': 'b', 'x': 'y'}  # dicionario com os dados do dataseries
my_series2 = pd.Series(my_dict) # criando o dataseries 

print(my_series2)   # exibindo o dataseries
print(f'type {type(my_series2)}')   # exibindo o tipo do objeto my_dataseries2

# --------------------------------------------------------------------------------

# criando a partir de uma tupla 
my_tuple = (4, 5, 6)
my_series3 = pd.Series(my_tuple)

print(my_series3)
print(type(my_series3))
