from random import randrange
numsecreto = randrange(0, 10)
tentativas = 0
continuar = 'S'
numero = 0
while numsecreto != numero:
    numero = int(input('Digite um valor: '))
    if numero == numsecreto:
        print('Parabens voce acertou!')
        tentativas += 1
    else:
        print('Errou!')
        tentativas += 1
print('Voce jogou {} vezes'.format(tentativas))