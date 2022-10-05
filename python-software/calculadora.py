res = 's'
while res == 's':
    n1 = int(input('Digite um valor:'))
    sin = str(input('Digite um sinal:'))
    n2 = int(input('Digite mais um número:'))
    res = str(input('Você quer continuar? [s/n]'))

#aqui eu apenas coloquei uma condição, para se caso o usuário escolha algum sinal, então o código iria ler
#e escolher entre, por exemplo: se o usuário escolhesse +, então o algoritmo faria n1 + n2, e jogaria para
#uma váriavel chamada resultado, onde eu mando imprimir na tela.
if sin == '+':
    resultado = n1 + n2 
elif  sin == '-':
    resultado = n1 - n2
elif sin == '*':
    resultado = n1 * n2
elif sin == '/':
    resultado = n1 / n2

#aqui o negócio complica para eu explicar, pois tive uma epifania momentanea que logo perdi, pois fui
#distraido com ruidos externos;

# bem eu peguei o resultado de por exemplo 1 + 1, e depois deixei a trabalho do algoritmo em escolher
# se na frente deste algoritmo teria mais números, como: 10 + 10 (primeira parte) + 10 + 10 (segunda parte)
# ou quer continuar, e então se o resultado fosse igual a esses números, ele pegaria o resultado n1 + n2 e 
# jogaria para a váriavel resutado, que teria um novo resultado. que no caso seria 40.

# if resultado ==  n1 + n2:
#     resultado = resultado + n1 + n2 
# elif resultado == n1 - n2:
#     resultado = resultado - n1 - n2
# elif resultado == n1 * n2:
#     resultado = resultado * n1 * n2
# elif resultado == n1 / n2:
#     resultado = resultado / n1 / n2


print(f'{resultado}')
