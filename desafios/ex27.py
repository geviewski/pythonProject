nome = str(input('Digite seu nome: ')).strip()
primeiro_nome = nome.split()
print('Seu primeiro nome é: {}'.format(primeiro_nome[0].title()))
print('Seu ultimo nome é: {}'.format(primeiro_nome[len(primeiro_nome)-1].title()))