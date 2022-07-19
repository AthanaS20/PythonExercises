numero = int(input('Digite um número:'))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    
    print('{}'.format(c), end=' ')
    calculo = numero % numero == 0

print('O numéro {} é divísel {} vezes, logo ele é PRIMO'.format(numero,tot))
