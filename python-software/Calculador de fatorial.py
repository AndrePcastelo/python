#Calculadora de Fatorial Simples
import numpy

c = 's'
res = 's'
lista = []
lista2 = []
a = int(input('Digite um número:'))
res = str(input('Você quer adicionar um número fatorial repetido? [s/n]'))
if res == 's':
    while c == 's':
     lista2.append(int(input('Digite o número repetido:')))
     c = str(input('Voce quer adicionar mais um número? [s/n]'))
for a in range(a, 0, -1):
    print(f'{a}.')
    lista.append(a)
for lista2 in range (lista2[0], 0, -1):
    print(f'{lista2}.')
print(lista)
print(numpy.prod(lista))
print(lista2)

