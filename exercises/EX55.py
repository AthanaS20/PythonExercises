maiorPeso = 0
menorPeso = 0
for peso in range(1, 6):
    pessoa = float(input('Peso da {}º pessoa em KG: '.format(peso)))
    if peso == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if pessoa > maiorPeso:
            maiorPeso = pessoa
        if pessoa < menorPeso:
            menorPeso = pessoa
print('O maior peso é {} KG.'.format(maiorPeso))
print('O menor peso é {} KG'.format(menorPeso))


    