km = int(input('Digite o valor do km para saber o valor da passagem: '))
if km > 200:
    tot_km = km * 0.45
    print('O valor da passagem é: R$:{:.2f}'.format(tot_km))
else:
    tot = km * 0.50
    print('O valor da passagem é: R$:{:.2f}'.format(tot))