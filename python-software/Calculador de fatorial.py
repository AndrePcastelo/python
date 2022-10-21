#Calculadora de Fatorial Simples
import numpy

lista = []
a = int(input('Digite um número:'))
print(f'A fatorial deste {a}! número é: ')
for a in range(a, 0, -1):
    print(f'{a}.')
    lista.append(a)
print(lista)
print(numpy.prod(lista))
