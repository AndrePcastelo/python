from datetime import date
ano = int(input('Que ano quer analisar?, coloque 0 para colocar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Este ano {ano} é bissexto!')
else: 
    print(f'Este ano {ano} não é bissexto!')