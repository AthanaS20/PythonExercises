numeros = []
for valores in range(0,5):
    numeros.append(int(input('Digite um número:')))
print('=' * 40)
print(f'Sua lista tem os seguintes valores {numeros}')

print(f'O maior valor digitado foi {max(numeros)} que está na {numeros.index(max(numeros))+1} º posição.')
print(f'O menor valor digitado foi {min(numeros)} que está na {numeros.index(min(numeros))+1} º posição.')    