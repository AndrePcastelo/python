#Calculadora de Fatorial Simples
import numpy

lista = []
a = int(input('Digite um número:'))
for a in range(a, 0, -1):
    print(f'{a}.')
    lista.append(a)
print(lista)
print(numpy.prod(lista))
