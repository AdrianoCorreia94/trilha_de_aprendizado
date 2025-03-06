# tokenizacao: quebrar/separar o texto em palavras
texto = 'esse é o texto para tokenizacao'
token = texto.split()
print(token)

# PADRONIZACAO 
# colocar as palavras em um formato padrao, por exemplo, padronizar girias e abreviacoes 
# td = tudo 
# 9idade = novidade
# vc = voce

# SEGMENTACAO 
# dividir um fragmento de texto como um parágrafo em frases/sentencas,

# REGRA UNÁRIA
'''
    cada no contem apenas 1 filho
    exemplo:
        A -> B, C será convertido em A-> B+C
    
'''

# FORMA NORMAL DE CHOMSKY - CNF
'''
    Cada nó com no máximo 2 filhos
    exemplo:
        A -> B, C, D 
        será convertido em 
        A-> B, X
        X-> C, D
'''
