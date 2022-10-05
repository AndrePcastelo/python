n1 = int(input('Digite um número, e então descobriremos se ele é par ou ímpar: '))
resultado = n1%2

if resultado == 0:
    print(f'O {n1} é par')
else:
    print(f'O {n1} é ímpar')