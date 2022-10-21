from random import randint
cont = 0
lista = []
jogos = []
tot = 1

print('*' * 30)
print('    SORTEIRO MEGA SENA    ')
print('*' * 30)

quant = int(input('Quantos jogos você quer sortear?'))

while tot <= quant:
    cont += 0
    while True:

        numero = randint(0, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
        
    lista.sort()
    jogos.append(lista[:])
    tot += 1
print(f'Os Jogos sorteados foram: {jogos}')

