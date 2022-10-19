lista = []


for num in range(1,8):
    lista.append(int(input(f'Digite o {num}º valor:')))
    

for valores in lista:
    if valores % 2 == 0:
        print(lista)
