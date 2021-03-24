nome = str(input('Qual é seu nome: '))
if nome == 'henrique':
    print('que nome bonito voce tem!')
elif nome == 'felipe' or nome == 'igor' or nome == 'guilherme' or nome == 'rodrigo':
    print('Seu nome é bem popular!')
else:
    print('que nome normal voce tem!')
print('boa noite {}, seja bem vindo!'.format(nome))