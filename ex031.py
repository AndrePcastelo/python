km = float(input('Qual a distância de sua viagem?:'))
print(f'Você está preste a viajar {km}km')

tarifa = km * 0.50
tarifa2 = km * 0.45

if km > 0 and km < 200:
    print(f'Você pagará ${tarifa:.2f} Reais')
elif km > 200:
    print(f'Você pagará ${tarifa2:.2f} Reais')
else:
    print('Você não pagará nada')