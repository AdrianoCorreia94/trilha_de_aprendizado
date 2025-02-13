from datetime import timedelta, datetime

carro_p = 35
carro_m = 43
carro_g = 54

tamanho_carro = input('Tamanho do veículo \nP - pequeno \nM - medio \nG - grande')


if tamanho_carro in 'pP':
    chegada = datetime.now()
    entrega = chegada + timedelta(minutes= carro_p)
    print(f'O carro chegou em {chegada} e deverá ser entregue em {entrega}')
elif tamanho_carro in 'Mm':
    chegada = datetime.now()
    entrega = chegada + timedelta(minutes= carro_m)
    print(f'O carro chegou em {chegada} e deverá ser entregue em {entrega}')
elif tamanho_carro in 'Gg':
    chegada = datetime.now()
    entrega = chegada + timedelta(minutes= carro_g)
    print(f'O carro chegou em {chegada} e deverá ser entregue em {entrega}')
else:
    print('Tamanho de carro nao reconhecido ')

# criar um dicionario para armazenar a data como chave 
# os valores dentro de cada chave é o horario

