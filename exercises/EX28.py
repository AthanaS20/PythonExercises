import random
n = int(input('Advinhe qual número escolherei de 0 a 5!'))
n2 = random.randint(0,5)
print('O número escolhido foi {}'.format(n2))
if n == n2:
    print('PARABÉNS, VOCÊ ME VENCEU!')
else:
    print('AH QUE PENA! AINDA NÃO FOI DESSA VEZ!')


