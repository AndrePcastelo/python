r1 = float(input('Digite a medida da primeira reta:'))
r2 = float(input('Digite a medida da segunda reta:'))
r3 = float(input('Digite a medida da terceira reta:'))

maiorlado = r1
if r2 > r1 and r2 > r3:
    maiorlado = r2
elif r3 > r1 and r3 > r2:
    maiorlado = r3
if maiorlado > r2 + r3:
    print('Não é possivel formar um triângulo')
elif maiorlado > r3 + r1:
    print('Não é possivel formar um triângulo')
elif maiorlado > r1 + r2:
    print('Não é possivel formar um triângulo')
if maiorlado < r2 + r3:
    print('É possivel formar um triângulo')
elif maiorlado < r3 + r1:
    print('È possivel formar um triângulo')
elif maiorlado < r1 + r2:
    print('È possivel formar um triângulo')

