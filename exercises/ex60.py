from math import factorial
numero = int(input('Digite um valor para ver o fatorial do número:'))
contador = numero
fatorial = factorial(numero)
print('Calculando fatorial de {}!'.format(numero))
while contador > 0:
    print('{}'.format(contador), end= '')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1
print('{}'.format(fatorial))

    
