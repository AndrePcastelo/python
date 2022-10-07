#Números mutiplos de 3
contador = 0
soma = 0
for n in range (1,500, 2):
   if n % 3 == 0:
    print(n)
    contador = contador + 1
    soma = soma + n
print('-' *30)
print(f'O resultado é:{soma}, e a quantidade de números impares divisiveis por 3 são {contador}')