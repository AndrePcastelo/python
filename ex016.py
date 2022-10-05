import emoji
import math
print(emoji.emojize('seja bem vindo meu caro :beating_heart:', use_aliases=True))
name = input('diga-me o seu nome meu caro')
print('>'*200)
print(f'seja bem vindo {name} ')
print('>'*200)
print(emoji.emojize('Vamos usar o nosso calculador ? :brain:', use_aliases=True))
n1 = float(input('Digite um numero por favor caro'))
print(f'O seu numero é {n1} \n o inteiro dele é {math.trunc(n1)}')


