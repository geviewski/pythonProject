contador = 0
soma = 0
print('Somatória de números automatico: [Digite 999 para parar!] ')
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    contador += 1
    soma +=n
print(f'Voce digitou {contador} números e a soma deles é {soma}')