import random
a = input('Digite o primeiro nome:')
b = input('Digite o segundo nome:')
c = input('Digite o terceiro nome:')
d = input('Digite o quarto nome:')
s = a, b, c, d
print('Parabéns {} você foi sorteado, acaba de ganhar um SAMSUNG S10 NOVINHO!!'.format(random.choice(s)))