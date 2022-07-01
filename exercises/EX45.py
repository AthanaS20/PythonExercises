from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' 
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Escolha sua jogada:'))
print(''' 
JO
KEN
PO!! ''' )
print('=*' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('=*' * 15)

if computador == 0 and jogador == 0:
    print('O Jogo deu EMPATE!')
elif computador == 1 and jogador == 1:
    print('O jogo deu EMPATE!')
elif computador == 2 and jogador == 2:
    print('O jogo deu EMPATE!')
elif computador == 0 and jogador == 1:
    print('COMPUTADOR GANHOU!')
elif computador == 1 and jogador == 0:
    print('COMPUTADOR GANHOU!')
elif computador == 2 and jogador == 1:
    print('COMPUTADOR GANHOU!')
elif computador == 1 and jogador == 2:
    print('JOGADOR GANHOU!')
elif computador == 0 and jogador == 2:
    print('COMPUTADOR GANHOU!')
elif computador == 2 and jogador == 0:
    print('JOGADOR GANHOU!')

