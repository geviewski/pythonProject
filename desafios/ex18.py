from math import sin, cos, tan
numero = int(input('Digite o valor do angulo: '))
#seno = sin(numero)
#cosseno = cos(numero)
#tangente = tan(numero)
#print('O valor do angulo é {} e o seu seno é {:.3} o cosseno {:.3} e a tangente é {:.3}'.format(numero, seno, cosseno, tangente))
print('O valor do angulo é {} e o seu seno é {:.3} o cosseno é {:.3} e a tangente é {:.3}'.format(numero, sin(numero), cos(numero), tan(numero)))