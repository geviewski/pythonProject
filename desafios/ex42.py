lado1 = int(input('Digite o Primeiro numero: '))
lado2 = int(input('Digite o Segundo numero: '))
lado3 = int(input('Digite o terceiro numero: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os numeros podem formar um triangulo ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILATERO!!')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO!!')
    else:
        print('ISÓSCELES!')
else:
    print('Os numeros nao podem formar um triangulo')