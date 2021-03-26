primeiro = int(input('Primeiro elemento: '))
razao = int(input('Razão: '))
n = int(input('Quantos elementos exibir: '))
ultimo = primeiro + (n - 1) * razao
ultimo += ultimo
for var in range(primeiro, ultimo, razao):
    print(var)