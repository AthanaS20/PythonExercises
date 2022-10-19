temporaria = []
principal = []
maior = menor = 0


while True:
    temporaria.append(input('Digite o seu nome:'))
    temporaria.append(int(input('Digite o peso KG:')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]

    principal.append(temporaria[:])
    principal.clear()
    
    resposta = input('Deseja prosseguir? [S/N]').upper().lower()[0]
    
    
    if 'n' in resposta:
        break
    
      
print(f'Você cadastrou {len(principal)} pessoas.')
print('As pessoas com maior peso são: ',end=' ')
for pessoas in principal:
    if pessoas[1] == maior:
        print(pessoas[0])
print('As pessoas com menor peso são: ',end=' ')
for pessoas in principal:
    if pessoas[1] == menor:
        print(pessoas[0])







