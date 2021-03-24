nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Aluno reprovado! Sua media é {}'.format(media))
if media>=5 and media<=6.9 :
    print('Aluno em recuperação! Sua media é {}'.format(media))
if media >= 7:
    print('Aluno aprovado! Sua media é {}'.format(media))