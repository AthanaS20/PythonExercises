soma = 0
cont = 0
for num in range(1, 501):
    if num % 2 !=0:
        if num % 3 ==0:
            soma = num + soma
            count = count + 1
print('A soma dos {} valores informados é igual a {}'.format(cont, soma))
 #Peguei o cont e soma na resolução do exercicio   
    
