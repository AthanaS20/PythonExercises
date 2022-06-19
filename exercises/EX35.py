print('=-' * 12)
print('ANALISANDO SEU TRIANGULO')
print('=-' * 12)

segA = float(input('Primeiro Segmento:'))
segB = float(input('Segundo Segmento:'))
segC = float(input('Terceiro Segmento:'))

if segA + segB > segC and segC + segB > segA:
    print('Com os valores apresentados, podemos formar uma triangulo!')
else:
    print('Infelizmente não podemos formar um triangulo com esses valores!')

