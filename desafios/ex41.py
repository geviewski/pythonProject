from datetime import date
ano_atual = date.today().year
data_nasc = int(input('Digite a data de nascimento do competidor para ver em qual grupo ele se encaixa: '))
data = ano_atual - data_nasc
if data <= 9:
    print('Voce tem {} anos e está na categoria: Mirin!'.format(data))
elif data > 9 and data <= 14:
    print('Voce tem {} anos e está na categoria: Infantil!'.format(data))
elif data > 14 and data <= 19:
    print('Voce tem {} anos e está na categoria: Junior!'.format(data))
elif data > 19 and data <=25:
    print('Voce tem {} anos e está a categoria: Sênior!'.format(data))
else:
    print('Voce tem {} anos e está na categoria: Master!'.format(data))