numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
escolhas = 'S'
while escolhas == 'S':
    escolhas = int(input(''' Faça uma escolha:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair do programa '''))
    if escolhas == 1:
        soma = numero1 + numero2
        print(' Os valores informados foram {} e {} e a soma deles é {}'.format(numero1, numero2, soma))
        escolhas = str(input('Voce quer continuar? [S/N] ')).upper()
    elif escolhas == 2:
        multiplicar = numero1 * numero2
        print(' Os valores informados foram {} e {} e a nultiplicação deles é {}'.format(numero1, numero2, multiplicar))
        escolhas = str(input('Voce quer continuar? [S/N] ')).upper()
    elif escolhas == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print('Os valores informados foram {} e {} e o maior numero é {}'.format(numero1, numero2, maior))
        escolhas = str(input('Voce quer continuar? [S/N] ')).upper()
    elif escolhas == 4:
        numero1 = int(input('Digite o primeiro novo valor: '))
        numero2 = int(input('Digite o segundo novo valor: '))
        print('Os novos valores informados são: {} e {}'.format(numero1, numero2))
        escolhas = str(input('Voce quer continuar? [S/N] ')).upper()
    elif escolhas == 5:
        print('Obrigado por usar este programa! :D')
    else:
        print('ERRO!!')
        escolhas = str(input('Voce quer continuar? [S/N]')).upper()
print('fim!')