class Animal:
    def __init__(self, nro_patas):
        self.numero_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{k} {v}'for k, v in self.__dict__.items()])}"

# classes filhas 
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_pena, **kw):
        super().__init__(**kw)
        self.cor_pena = cor_pena
        

class Gato(Mamifero):
    pass    # posso utilizar o pass ou entao o init 

class Cachorro(Mamifero):
    pass    # modelo usando o pass

class Leao(Mamifero):
    def __init__(self, **kw):   # modelo utilizando o init 
        super().__init__(**kw) 

class Ornitorrico(Mamifero, Ave):
    pass

# instancias

g = Gato(cor_pelo='preto', nro_patas=4) # para kargs, os parametros devem ser nomeados
print(g)

o1 = Ornitorrico( nro_patas=2 , cor_pelo='Preto', cor_pena='Amarela')   
print(o1)


l = Leao(nro_patas=4, cor_pelo='amarela')
print(l)