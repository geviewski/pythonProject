peso = int(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / altura**2
if imc <= 18.5:
    print('seu peso é {:.2f}kg e voce está abaixo do peso!'.format(imc))
if imc > 18.5 and imc <= 25:
    print('Seu peso é {:.2f}kg e voce está com o Peso ideal!'.format(imc))
if imc > 25 and imc <= 30:
    print('Seu peso é {:.2f}kg e voce está com Sobrepeso!'.format(imc))
if imc > 30 and imc <= 40:
    print('Seu peso é {:.2f}kg e voce está com Obesidade!'.format(imc))
if imc > 40:
    print('Seu peso é {:.2f} e voce está com Obesidade Morbida!'.format(imc))