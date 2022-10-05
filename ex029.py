km = float(input('Qual a sua velocidade atual?:'))
multa = (km-80) * 7

if km > 80:
    print(f'Você ultrapassou o limite de velocidade, então terá de pagar {multa} reais')
else:
    print('Vá em paz com Deus, você não ultrapassou a velocidade')