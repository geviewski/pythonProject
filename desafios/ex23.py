#teste para fazer em str
#numero = str(input('Digite um numero: '))
#print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numero[3], numero[2], numero[1], numero[0]))
num = int(input('Informe um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))