# booleanos falsos
print(bool(0))   # numero zero (int)
print(bool(0.0)) # numero zero (float)
print(bool([]))  # lista vazia
print(bool({}))  # dict vazio
print(bool(None)) # None
print(bool(''))  # string vazia

# booleanos verdadeiros
print(bool(-345))   # numero diferente de zero
print(bool('a'))    # string nao vazia 
print(bool(['a',2]))    # lista nao vazia
print(bool({'x':3}))    # dicionario nao vazio
print(bool(('a','b')))  # tuplas nao vazias
