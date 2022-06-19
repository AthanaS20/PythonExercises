import math
from math import asin, cos, atan
a = float(input('Digite um angulo:'))
s = asin(math.radians(a))
c = cos(math.radians(a))
t = atan(math.radians(a))
print('O angulo de {} tem o SENO de {:.2f} \n O agulo de {} tem o COSSENO de {:.2f} \n O angulo de {} tem a TANGENTE DE {:.2f}'
      .format(a, s, a, c, a, t))
