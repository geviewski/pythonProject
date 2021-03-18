ano = int(input('digite o ano: '))
if (ano%4==0 and ano%100!=0):
    print('Ano bissexto')
else:
    print('Não é bissexto')