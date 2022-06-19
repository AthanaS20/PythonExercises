numero = int(input('Digite um número inteiro qualquer:'))
print('Escolha a conversão que deseja realizar:')
print('[1] Para converter em BINÁRIO \n[2] Para converter em OCTAL\n[3] Para converter em HEXADECIMAL')
escolha = int(input('A opção escolhida foi:  '))
if escolha == 1:
    print('{} O número em BINÁRIO é {}'.format(numero, bin(numero)))
elif escolha == 2:
    print('{} O número em OCTAL é {}'.format(numero, oct(numero)))
elif escolha == 3:
    print('{} O número em HEXADECIMAL é {}'.format(numero, hex(numero)))

