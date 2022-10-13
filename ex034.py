import time
salario = int(input('Digite o seu salário atual:'))

if salario > 1250:
    newsal = salario + (10/100 * salario)
elif salario < 1250:
    newsal = salario + (15/100 * salario)
else:
    newsal = salario
print(f'O seu salario atual é {salario}')
time.sleep(1)
print(f'Salario com bonus R${newsal}')

