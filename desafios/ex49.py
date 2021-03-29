num = int(input('\033[0;35;40m Digite um numero: \033[m '))
for c in range(0, 11):
    print('\033[0;35;40m {} x {} = {} \033[m'.format(num, c, num*c))
print('\033[0;35;40m Fim! \033[m')