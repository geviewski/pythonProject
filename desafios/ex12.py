reais= float(input('Digite o valor do produto: '))
print('O valor do produto é R$:{} e com 5% de desconto fica por R$:{:.5}'.format(reais, reais - (reais * 5/100)))