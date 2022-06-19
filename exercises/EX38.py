numero = int(input('Digite um número:'))
numero2 = int(input('Digite outro número:'))
if numero > numero2:
    print('O PRIMEIRO número escolhido é maior que {}!.'.format(numero2))
elif numero < numero2:
    print('O SEGUNDO número escolhido é maior que {}'.format(numero))
elif numero == numero2:
    print('Os DOIS número são IGUAIS')
else:
    print('Valor ínválido, tente novamente.')