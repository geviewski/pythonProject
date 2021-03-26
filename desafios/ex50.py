s = 0
for c in range(0, 6):
    num = int(input('Digite o {}° numero: '.format(c+1)))
    if num % 2 == 0:
        s +=num
print(s)