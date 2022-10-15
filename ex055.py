maiorpeso = 0
menorpeso = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}° pessoa: '))
    if peso > peso:
        maiorpeso = maiorpeso + peso
    elif peso < peso:
        menorpeso = menorpeso +  peso
print(f'A pessoa mais pesada possui: {maiorpeso}kg e a mais leve possui: {menorpeso}kg')