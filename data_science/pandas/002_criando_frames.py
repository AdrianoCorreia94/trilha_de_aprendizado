import pandas as pd 

# criando a partir de um dicionario 

my_dict = {
           'A': [1, 2 ,3], 
           'B': [9, 8, 7], 
           'C': [2, 4, 6], 
           'D': [1, 3, 5]
           }

frame1 = pd.DataFrame(my_dict)
print(frame1)