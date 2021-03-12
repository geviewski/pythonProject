from random import choices
print('vamos escolher um nome para apagar o quadro: ')
alunos = ('henrique', 'gabriel', 'fernando', 'kelly')
escolha = choices(alunos)
print('O aluno selecionado foi: {} '.format(escolha))