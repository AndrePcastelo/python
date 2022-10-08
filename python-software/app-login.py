#Cadastro de novas contas, com login e senha

import time
def lin():
    print('-'*30)


print('Área de cadastro')
lin()
usuario = input('Cadastre o seu usuário:')
senha = int(input('Digite a sua senha:'))
lin()
print('Cadrasto feito!')
res = str(input('Você quer fazer login?: [s/n]'))
if res == 's':
    print('carregando...')
    time.sleep(3)
    loginus = input('Usuario:')
    loginse = int(input('Senha:'))
    if loginus == usuario and loginse == senha:
        print(f'Seja bem vindo: {usuario}')
    else:
        print('Senha ou usuario incorreto')
else:
    print('Ate mais tarde!')
    