from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(0, 7):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas MAIORES de idade!'.format(totmaior))
print('E tambem tivemos {} pessoas MENORES de idade!'.format(totmenor))