from time import sleep

soma = 0
quan = int(input('Quantos números você quer colocar?:'))
for c in range(1, quan + 1):
    n1 = int(input(f'Digite o {c} número:'))
    sleep(1)
    soma = soma + n1
print(f'A soma desses números é: {soma}')
