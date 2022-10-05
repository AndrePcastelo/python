dias =int(input('me diga quantos dias voce alugou o carro?'))
km = int(input(' me diga quantos km percorreu'))
d = dias * 60
k = d + (km * 0.15)
print(f'o novo preço a pagar será R${k:.2f}')
