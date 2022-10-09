
contador = numeroUsuario = soma = 0    
numeroUsuario = int(input('Digite um valor [Digite 999 para interromper o LAÇO]:'))
while numeroUsuario != 999:   
    soma = soma + numeroUsuario
    contador += 1 
    numeroUsuario = int(input('Digite um valor [Digite 999 para interromper o LAÇO]:'))
print('Você digitou {} números e a soma entre eles é de {}'.format(contador, soma))
    
    


    
        
        

    