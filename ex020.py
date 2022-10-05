import random
n1 = str(input('Nome do primeiro aluno:'))
n2 = str(input('Nome do segundo alundo:'))
n3 = str(input('Nome do terceiro alundo:'))
n4 = str(input('Nome do quarto aluno:'))
list = [n1, n2, n3, n4]
random.shuffle(list)
print(f'a sua lista é:')
print(list)
#shuffle serve para embaralhar os itens, então ele embaralha e o print mostra.
# se eu quizesse economizar espaço eu poderia usar= from random import shuffle

# outra maneira de fazer esse exercício seria:
# n1 = str(input('Diga um nome:))
# list = [n1, ....]
# print('A sua lista embaralhada é {random.sample(list,k=4)})
