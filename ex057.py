#validador de sexos 
s = str(input('Digite o seu sexo: [M/F]')).strip().upper()[0]
while s != 'm' and s != 'f':
    s = str(input('Digite o seu sexo novamente:')).strip().upper()[0]
if s == 'm':
    print(f'Sexo masculino cadastrado: {s}')
else:
    print(f'Sexo feminino cadastrado: {s}')
    
