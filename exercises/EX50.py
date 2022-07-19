soma = 0
for numero in range(1, 7):
    numero = int(input('Digite um valor:'))
    if numero % 2 == 0:
        soma = numero + soma
print('A soma dos número pares é {}.'.format(soma))
    


