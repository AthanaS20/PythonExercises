numero = soma = 0

while True:
    numero = int(input('Digite um numero:'))
    if numero == 999:
        break
    soma = soma + numero
print('A soma é {}'.format(soma))