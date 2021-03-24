from datetime import date
ano = date.today().year
idade = int(input('Digite o ano de seu nascimento para sabermos se voce ira se alistar ou se ja passou o tempo de se alistar: '))
alistamento = ano - idade
if alistamento >= 19:
    print('Voce tem {} anos e perdeu o alistamento!'.format(alistamento))
if alistamento == 18 :
    print('Voce tem {} anos e esta na hora de voce se alistar!'.format(alistamento))
elif alistamento < 18:
    print('Voce tem {} anos e ainda não tem idade suficiente para se alistar!'.format(alistamento))