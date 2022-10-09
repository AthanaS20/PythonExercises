from random import randint

print('=*' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=*' * 13)

computador = randint(1, 20)
soma = par = impar = resultado = 0
escolha = 'IMPAR' 'PAR'
numero = int(input('Digite um valor:'))
escolha = input('ESCOLHA [PAR/IMPAR]:')


while True:
    
    print(f'Você escolheu {numero} e o computador escolheu {computador}.')    
    resultado = soma = numero + computador
    print(f'O TOTAL foi {soma} o resultado é ', end='')
    if soma % 2 == 0:
        print('PAR')
        if escolha in 'PAR':
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    elif soma % 2 == 1:
        print('IMPAR')
        if escolha in 'IMPAR':
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    
    
    
    


    '''print(f'O TOTAL foi {soma} o resultado é ', end='')
    if soma % 2 == 0:
        print('PAR')
    if soma % 2 == 1:
        print('IMPAR')
    if escolha != resultado:
        print('Não foi dessa vez!')
        break
    elif escolha == resultado:
        print('PARABÉNS, VOCÊ VENCEU!')'''




