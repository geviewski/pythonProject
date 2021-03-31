c = 'S'
while c == 'S':
    sexo = str(input('Digite seu sexo: \033[1;34m[M/\033[1;35mF]')).upper()
    if sexo == 'M' or sexo == 'F':
        print('\033[32m Ok! Resposta correta!\033[m')
        c = str(input('Deseja continuar? \033[1;32m[S/\033[1;31mN]\033[m')).upper()
    else:
        print('\033[1;31mErrou\033[m')
        c = str(input('Deseja continuar? \033[1;32m[S/\033[1;31mN]\033[m')).upper()
print('Fim')