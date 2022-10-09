from random import randint
contador = 0

while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0, 20)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('PAR ou ÍMPAR [P/I]?').upper().strip()[0]
    print(f'Você escolheu {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu, o numero é PAR')
            contador += 1
        else:
            print('Você perdeu, o número é PAR!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu, o número é ÍMPAR!')
            contador += 1
        else:
            print('Você perdeu, o número é ÍMPAR!')
            break
    print('Vamos jogar mais uma vez?')
print(f'Você jogou {contador} vezes')