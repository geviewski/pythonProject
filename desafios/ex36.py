salario = float(input('Digite seu salario: R$:'))
valor_imovel = float(input('Digite o valor do imovel: R$:'))
parcela = int(input('Digite em quantos meses voce quer financiar: '))
tot_valor = valor_imovel / parcela
if tot_valor >= (salario * 30/100):
    print('O valor da parcela está acima do limite de 30% da sua renda, por tanto o financiamento foi negado.')
    print('Seu salario é R$:{} e o valor da parcela é de R$:{:.2f}.'.format(salario, tot_valor))
else:
    print('Parabens, financiamento aprovado! Seu salario é R$:{} e o valor da parcela é R$:{:.2f}'.format(salario, tot_valor))