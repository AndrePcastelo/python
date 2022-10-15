pares = 0
numbers = 0
soma = ArithmeticError
for c in range (1, 7):
    numbers = int(input(f'Digite o número {c}.'))
    if numbers % 2 == 0:
        pares = pares + 1
        soma = soma + numbers
print(f'A quantidade de números pares é: {pares}')
print(f'Soma entre os numeros pares {soma}')
