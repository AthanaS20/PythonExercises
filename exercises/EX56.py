somaIdade = 0
mediaIdade = 0
for dados in range(1, 5):
    print('--- {}º PESSOA ---'.format(dados))
    nome = input('NOME:')
    idade = int(input('IDADE:'))
    sexo = input('SEXO [F/M]:')
    somaIdade = somaIdade + idade 
mediaIdade = somaIdade / 4
print('A média das IDADES entre as pessoas é {}.'.format(mediaIdade))