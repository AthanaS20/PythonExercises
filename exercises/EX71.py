
print('*' * 20)
print('    BANCO INVEST   ') 
print('*' * 20)

#Não consegui chegar a nenhuma conclusão, resposta do professor a seguir
saque = int(input('Qual valor você quer sacar? R$'))
cedula = 50
totalced = 0
total = saque

while True:
    
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de {cedula} R$')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break

