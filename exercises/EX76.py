from turtle import pos


print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)

listaEscolar = ('\nLápis', 1.90,
                'Caneta', 2.00,
                'Caderno', 10.50,
                'Estojo', 11.00,
                'Corretivo',5.00,
                'Apontador', 2.50,
                'Mochila', 50.00,
                'Livro', 25.00,)
for posição in range(0,len(listaEscolar)):
    if posição % 2  == 0:
        print(f'{listaEscolar[posição]:.<30}',end='')
    else:
        print(f'R${listaEscolar[posição]:.>4.2f}')