palavras = ('AMOR','CARINHO','PROGRAMAÇAO','DEDICAÇAO','TEMPO','DINHEIRO')


for vog in palavras:
    print(f'Nas palavras {vog} temos as vogais:')
    for letra in vog:
        if letra.lower() in 'aeiou':
            print(letra)

        

      