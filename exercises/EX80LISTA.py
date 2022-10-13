numeros = []


for num in range(0,5):
    usuario = numeros.append(int(input('Digite um valor:')))
    if num == 0 or usuario > numeros[-1]:
        numeros.append(usuario)
    else:
        pos = 0
        while pos < len(numeros):
            if usuario <= numeros[pos]:
                numeros.insert(pos, usuario)
                break
            pos += 1

print(f'Os valores digitados são {numeros}')
    
