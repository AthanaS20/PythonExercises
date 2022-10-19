

lista = []
pares = []
impares = []


while True:
    usuario = lista.append(int(input('Type a value:')))
    
    
    continuar = input('Do you wanna keep moving? [Y/N]').upper().lower()[0]

    if 'n' in continuar:     
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A sua lista competa é {lista}')
print(f'A lista com números pares: {pares}')
print(f'A lista com números Impares: {impares}')

