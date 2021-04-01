primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
        total += mais
        while contador <= total:
            print(' {} ->'.format(termo), end='')
            termo += razão
            contador += 1
        print(' Pausa!!')
        mais = int(input('Quantos termos você quer mostras a mais? '))
print('FIM!!')