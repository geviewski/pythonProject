from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada: '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[computador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador ==1:
        print('Jogador vence')
    elif jogador ==2:
        print('Computador vence')
    else:
        print('Jogada invalida!')
elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador ==1:
        print('Empete')
    elif jogador ==2:
        print('Jogador Vence')
    else:
        print('Jogada invalida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador Vence')
    elif jogador ==1:
        print('Jogador Computador')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida!')
