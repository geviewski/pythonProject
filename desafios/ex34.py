salario = int(input('Digite o seu salario: '))
if salario >= 1250:
    aumento_salario = salario * 10 / 100
    print('o novo salario é de: R$:{:.2f}'.format(salario + aumento_salario))
else:
    aumento_salario = salario * 15 / 100
    print('o novo salario é de: R$:{:.2f}'.format(salario + aumento_salario))