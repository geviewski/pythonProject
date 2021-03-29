num = int(input('Digite um numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, total), end='')
if total == 2:
    print(' E por isso ele é um número PRIMO!')
else:
    print(' E por isso ele NÃO é um número PRIMO!')