segA = int(input('Digite o primeiro SEGMENTO:'))
segB = int(input('Digite o segundo SEGMENTO:'))
segC = int(input('Digite o terceiro SEGMENTO:'))
#calculoTriangulo = segA + segB > segC and segC + segB > segA
#if segA == segB and segB == segC and segA == segC:
if segA + segB > segC and segC + segB > segA:
    print('Com os SEGMENTOS informados, podemos criar um TRIÂNGULO', end= ' ')
    if segA == segB and segB == segC:
        print('EQUILATERO!')
    elif segA != segB and segB != segC and segC != segA:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Infelizmente, você não pode formar um TRIANGULO!')

