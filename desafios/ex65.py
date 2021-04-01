resp = 'S'
n = cont = totnum = maior = menor = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    totnum += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper()
media = totnum / cont
print('Voce digitou {} vezes e a media foi {}'.format(cont, media))
print('O maior número é {} e o menor é o {}'.format(maior, menor))
print('fim')