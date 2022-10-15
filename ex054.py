from datetime import date, time
maioridade = 0
menoridade = 0
anoatual = date.today().year
for c in range (1, 8):
    nasc = int(input(f'Digite o ano de nascimento da pessoa {c}°: '))
    idade = anoatual - nasc
    if idade > 21:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1

print(f'O numero de pessoas maiores de idade são: {maioridade} e o numero de pessoas em menoridade são: {menoridade}')
