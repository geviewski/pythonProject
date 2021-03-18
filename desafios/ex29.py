multa = int(input('digite a velocidade do seu carro: '))
if multa > 80:
    print('voce passou do limite de velocidade, voce vai ser multado.')
    valor = (multa - 80) * 7
    print('o todal que voce ira pagar é R$:{:.2f}'.format(valor))
else:
    print('voce esta na valocidade correta.')