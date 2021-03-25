valor = float(input('Digite o valor do produto: '))
forma_pag = str(input('''Digite a forma de pagamento:
 [ 1 ] Avista
 [ 2 ] avista cartão
 [ 3 ] 2x no carão
 [ 4 ] 3x ou mais '''))
if forma_pag in ('1'):
    disc = valor-(valor * 10/100)
    print('O valor sem desconto é: R${:.2f} e com desconto é: R$:{:.2f} e a forma de pagamento é avista.'.format(valor, disc))
if forma_pag in ('2'):
    disc = valor - (valor * 5/100)
    print('O valor sem desconto é: R${:.2f} e com desconto é: R$:{:.2f} e a forma de pagamento é avista no cartão.'.format(valor, disc))
if forma_pag in ('3'):
    print('O valor a ser pago é: R${:.2f} e voce pode fazer em ate 2x sem juros'.format(valor))
if forma_pag in ('4'):
    disc = valor + (valor * 20/100)
    print('O valor sem desconto é: R${:.2f} e o total a ser pago é: R${:.2f} e voce fazer em 3x ou mais'.format(valor, disc))