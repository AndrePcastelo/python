somaidade = 0
media = 0
femme = 0
maisvelho = 0
for c in range(1, 4):
    print(f'{c}ª Pessoa')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[m/f]: '))
    somaidade += idade
    if c == 1 and sexo == 'Mm':
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        femme += 1
media = somaidade / 4
print(f'A média de idade do grupo é {media}')
print(f'O nome do Homem é {nomevelho}, e a idade é {maisvelho}')
print(f'A quantidade de mulheres com menos de 20 anos é {femme}')

