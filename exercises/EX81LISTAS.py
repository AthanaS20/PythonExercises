valores = []
contador = 0
while True:
    usuario = int(input('Digite um valor:')) # Poderiamos colocar valores.append(int(input('Digite um valor:'))) Para solicitar os numeros.
    contador += 1
    valores.append(usuario)
    resposta = input('Quer prosseguir? [S/N]').upper().lower()[0]
    #Para achar a quantidade poderiamos usar o len(valores) e não o contador =+ 1

    

    if 'n' in resposta:
        if 5 in valores:
            print(f'O valor 5 foi digitado {valores.count(5)} vez')
        else:
            print('O valor 5 não foi digitado.')
    
        valores.sort(reverse=True)
        print(f'Você digitou {contador} valores.')
        print(f'A lista de forma decrescente: {valores}')
        break


