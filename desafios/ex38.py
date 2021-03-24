num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
maior = num2
if num1 > num2:
    maior = num1
    print('O maior numero é o {}'.format(maior))
maior = num1
if num2 > num1:
    maior = num2
    print('O maior numero é o {}'.format(maior))
if num1 == num2:
    print('os valores são iguais.')