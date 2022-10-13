res = 0
tenta = 0
while res != 5:
    res = int(input('Tente adivinhar no número que estou pensando de 0 a 10: '))
    if res != 5:
        tenta = tenta + 1
print(f'O número de tentativas para você acertar foram:{tenta}')
