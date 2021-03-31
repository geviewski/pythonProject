'''for c in range(0, 11):
    print(c, end=' ')
print('Fim!')

c = 0
while c < 11:
    print(c, end=' ')
    c += 1'''

for c in range(1,3):
    n = int(input('Digite um valor: '))
print(n)

n = 1
while n!= 0:
    n = int(input('Digite um valor:'))
print(n)

resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    resposta = str(input('Quer coninuar? [S/N] ')).upper()
print('Fim')

resposta = 'S'
while resposta == 'S':
    numero1 = int(input('Digite o primeiro valor: '))
    numero2 = int(input('Digite o segundo valor: '))
    total = numero1 + numero2
    resposta = str(input('Quer continuar?[S/N] ')).upper()
print(total)

resp = 'S'
while resp == 'S':
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        print('par')
        resp = str(input('Quer continuar?[S/N] ')).upper()
    else:
        print('impar')
        resp = str(input('Quer continuar?[S/N] ')).upper()
print('Acabou')

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print('Voce digitou {} números pares e {} números impares.'.format(par, impar))