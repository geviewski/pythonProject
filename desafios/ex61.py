primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} '.format(termo), end='')
    termo +=razao
    contador += 1
print('FIM!')