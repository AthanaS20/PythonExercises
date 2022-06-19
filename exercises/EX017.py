cco = float(input('Digite o comprimento do cateto oposto:'))
cca = float(input('Digite o comprimento do cateto adjacente:'))
#hyp = (cco+cca*1/2)
hyp = (cco ** 2 + cca ** 2) ** (1/2)
print('O valor do CCO é {} e o valor de CCA {}, logo a hipotenusa vale {:.2f}'.format(cco, cca, hyp))

