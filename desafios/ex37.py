num = int(input('Digite um numero: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)))
if opçao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)))
if opçao == 3:
    print('{} covertido para hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('ERRO!!! Tente novamente!!!')