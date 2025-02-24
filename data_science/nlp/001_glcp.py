# minha primeira aula pratica sobre NLP

# gramatica livre de contexto probabilistica 


# passo 1: instalar a biblioteca nltk

# importar modulos
import nltk
from nltk import CFG, Tree, induce_pcfg, Nonterminal

# sentencas a serem analisadas
s1 = 'A Terra é redonda'
s2 = 'Marte é um planeta rochoso'
s3 = 'Jupiter é um planeta gasoso '
s4 = 'A Lua é um satélite natural da Terra'

# definir a gramatica
grammar = CFG.fromstring("""
    S -> SN SV
    SN -> Substantivo | Adjetivo | Artigo Substantivo | Artigo Adjetivo Substantivo | Artigo Substantivo Adjetivo
    SV -> Verbo | Verbo SN | Verbo SN Advérvio | Verbo Preposição SN | Verbo SN Preposição SN
    Substantivo -> 'Terra' | 'Marte' | 'Jupiter' | 'Lua'| 'satélite'| 'planeta' 
    Artigo ->  'o' | 'a' | 'O' | 'A'| 'UM'| 'UMA' | 'um'| 'uma' | 'Um' | 'Uma'
    Adjetivo -> 'redonda' | 'rochoso' | 'gasoso' | 'natural' 
    Verbo -> 'é'
    Preposição -> 'de' | 'da' | 'das' | 'dos' | 'do' |                          
                         """)

#print('Gramatica', grammar)    # imprimir a gramatica
#print('gramar.start() =>', grammar.start())   

#print(grammar.productions())

# COBERTURA DOS TERMOS
'''
print('Cobertura das palavras de entrada por uma gramatica: ')
try:
    grammar.check_coverage(['um','Marte'])  # verificar se todas as palavras da lista se encontram no objeto grammar
    print('Todas as palavras cobertas')
except:
    print('Nem todas')

try:
    grammar.check_coverage(['duns','natural'])
    print('todas cobertas')
except:
    print('Algumas palavras nao cobertas')
'''

# Parsing
''' 
sent = s4.split()   # usar metodo split para a sentenca
parser = nltk.ChartParser(grammar)  # criar o parser, utilizando o metodo nltk.ChartParser e a gramatica como parametro

for tree in parser.parse(sent): # chamar o metodo parse para o parser, enviando a sentenca como parametro
    print(tree)

'''

# aprendizagem da GLCP

data = [s1, s2, s3, s4]

train = []

for s in data:
    print(f'\nSentença: {s}')
    sent = s.split()
    print(sent)
    parser = nltk.ChartParser(grammar)

    for tree in parser.parse(sent):
        temp = tree 
        print(f'Analise: {temp}\n')
        train.append(Tree.fromstring(str(temp)))
    
    print('Arvores sintaticas')
    print(train)        


# FORMA NORMAL DE CHOMSKY
productions = []

for tree in train:
    tree.collapse_unary(collapsePOS = False)    # remover branches A-B-C into A-B+C
    tree.chomsky_normal_form(horzMarkov = 2)    # remover a -> (b, c, d) into a->b, c+d->d
    productions += tree.productions()

print(f'\n\n\nPRODUCTIONS\n{productions}')

# obtendo a gramatica livre de contexto 
s = Nonterminal('S')
prob_grammar = induce_pcfg(s, productions)
print(f'\n\n\nProb Grammar\n{prob_grammar}')

# ALGORITMO DE VITERBI 
print('Algoritmo de Viterbi')
sample = 'A Terra é redonda'

test = sample.split()
viterbi_parser = nltk.ViterbiParser(prob_grammar)

for tree in viterbi_parser.parse(test):
    print(f'\n\n\n{tree}')