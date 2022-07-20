from more_itertools import strip


frase = input('Digite uma frase:').strip()
#reverse = frase[::-1]
#print(reverse)
#Usei pra reverter, mas não vai funcionar nesse programa.
separar = frase.split()
juntar = ''.join(separar)
inverter = ''
for palavra in range(len(juntar) -1, -1, -1):
    inverter += juntar[palavra]
print('O inverso de {} é {}'.format(inverter, juntar))
if inverter == juntar:
    print('A PALAVRA ESCOLHIDA É POLINDRONA')
else:
    print('A PALAVRA NÃO É POLINDRONA')


