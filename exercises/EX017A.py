import math
cco = float(input('Digite o comprimento do cateto oposto:'))
cca = float(input('Digite o comprimento do cateto adjacente'))
hip = math.hypot(cco, cca)
print('O valor da hipotenusa é {:.2f}'.format(hip))