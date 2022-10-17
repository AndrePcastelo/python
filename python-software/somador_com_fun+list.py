#somador com funcão e lista #17/10/2022
def somador(lista):
    lista
    s = sum(lista)
    return s

lista = []
for c in range (1, 4):
    numbers = int(input(f'Digite o {c}° número:')) 
    print(numbers)
    lista.append(numbers)
print(lista)
r = somador(lista)
print(r)
    

