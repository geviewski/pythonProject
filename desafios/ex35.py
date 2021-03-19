lado1 = float(input('Primeiro seguimento: '))
lado2 = float(input('Segundo seguimento: '))
lado3 = float(input('Terceiro seguimento: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os seguimento a cima PODEM FORMAR UM TRIANGULO! ')
else:
    print('Os seguimento a  cima NÃO PODEM FORMAR UM TRIANGULO! ')