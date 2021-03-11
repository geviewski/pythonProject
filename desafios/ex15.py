dias= int(input('Digite os dias do aluguel do carro: '))
km= int(input('Digite a quilometragem percorrida: '))
tot_dias= dias * 60
tot_km= km * 0.15
total= tot_dias + tot_km
print('Os dias de aluguel foram de {} e foram percorridos {}km e com isso o total a se pagar é R$:{}0'.format(dias, km, total))