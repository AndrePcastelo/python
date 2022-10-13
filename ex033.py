n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite só mais um:'))
if n1 > n2 and n1 > n3:
    maiornumero = n1
elif n2 > n1 and n2 > n3:
    maiornumero = n2
else:
    maiornumero = n3
if n1 < n2 and n1 < n3:
    menornumero = n1
elif n2 < n1 and n2 < n3:
    menornumero = n2
else:
    menornumero = n3
print(f'O maior número é {maiornumero} e o menor número é: {menornumero}')
    
    
