import random
pc = random.randint(0 , 10)
acerto = False
jogadas = 0
print('Escolherei um número de 0 a 10, será que você consegue advinhar?')
while not acerto:
    palpite = int(input('Qual a sua jogada?'))
    jogadas += 1
    if palpite == pc:
        print('Parabéns!! Você acertou na {}º jogada!'.format(jogadas))
    if palpite > pc:
        print('Um pouco menos...')
    else:
        if palpite < pc:
            print('Um pouco mais...')

