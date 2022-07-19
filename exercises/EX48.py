soma = 0
cont = 0
for num in range(1, 501):
    if num % 2 !=0:
        if num % 3 ==0:
            soma = num + soma
            cont = cont + 1
print('A soma dos {} valores informados são igual a {}'.format(cont, soma))
    
    
