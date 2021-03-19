from random import randrange
aleatorio = randrange(0, 5)
numero = int(input('Digite um numero entre 0 a 5,   vejamos se é o mesmo que o do computador: '))
print('Analizando...')
if numero == aleatorio:
    print('Parabens voce acertou!')
else:
    print('Voce não acertou!')
print('o numero que o computador pensou foi o {} e o seu numero é {}'.format(aleatorio, numero))