numero1 = 0
numero2 = 0
escolhaUsuario = 0
pararPrograma = 0
#somar = 0
#multiplicar = 0
maiorNumero = 0
while pararPrograma != 5:
    if numero1 == 0 and numero2 == 0:
        numero1 = int(input('Digite o primeiro valor:'))
        numero2 = int(input('Digite o segundo valor:'))
    print(' [ 1 ] SOMAR \n [ 2 ] MULTIPLICAR \n [ 3 ] MAIOR \n [ 4 ] NOVOS NÚMEROS \n [ 5 ] SAIR DO PROGRAMA')
    escolhaUsuario = int(input('>>>>>>> Escolha uma OPÇÃO <<<<<<<<'))
    if escolhaUsuario == 1:
        somar = numero1 + numero2
        print('A soma entre {} e {} = {}'.format(numero1, numero2, somar))
    else:
        if escolhaUsuario == 2:
            multiplicar = numero1 * numero2
            print('A multiplicação entre {} e {} = {}'.format(numero1, numero2, multiplicar))
        if escolhaUsuario == 3:
            if numero1 > maiorNumero:
                maiorNumero = numero1
            if numero2 > maiorNumero:
                maiorNumero = numero2
            print('O maior número digitado é {}'.format(maiorNumero))
        if escolhaUsuario == 4:
            numero1 = 0
            numero2 = 0
    if escolhaUsuario == 5:
        print('===== FIM DO PROGRAMA =====')
    