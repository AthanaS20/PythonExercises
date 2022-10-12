

valores = list()



while True:
    
    valorUsuario = int(input('Digite um valor:'))
    if valorUsuario not in valores:
        valores.append(valorUsuario)
        print('Valor computado com sucesso...')
    else:
        print('O valor já foi computado, digite outro...')
    
    continuar = input('Você quer continuar [S/N]?').upper().lower()[0]
    
    if 'n' in continuar:
        valores.sort() #Não pode colocar o sort dentro da formatação, da erro np python e não mostra em ordem crescente.
        print(f'Os valores da sua lista são {valores}')
        break

        
