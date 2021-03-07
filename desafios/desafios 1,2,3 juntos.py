nome= input('Digite seu nome: ')
print('olá',nome,'! é um prazer em te conhecer!')
dia= input(nome+' em que dia voce nasceu? ')
mes= input(nome+' em que mes voce nasceu? ')
ano= int(input(nome+' em que ano voce nasceu? '))
print(nome,' voce nasceu na data de:',dia,'/',mes,'/',ano)
data_atual= int(input('em que ano nos estamos? '))
idade = data_atual - ano
print(nome,' voce tem',idade,'anos')
print(nome,' Por favor nos informe dois numeros: ')
numero1= int(input('Informe o primeiro numero: '))
numero2= int(input('Informe o segundo numero: '))
soma= numero1 + numero2
print(nome,' Os valores informados foram:',numero1,'e',numero2,'a soma entre eles é:',soma)