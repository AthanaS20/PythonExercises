respostaUsuario = 'S'
soma = media = contador = maiorNumero = menorNumero = 0
while respostaUsuario in 'Ss':
    numeroUsuario = int(input('Digite um valor:'))
    contador += 1
    soma = soma + numeroUsuario
    media = soma / contador

    if contador == 1:
        maiorNumero = numeroUsuario
        menorNumero = numeroUsuario
    else:
        if numeroUsuario > maiorNumero:
            maiorNumero = numeroUsuario
        if numeroUsuario < menorNumero:
            menorNumero = numeroUsuario     
    
    respostaUsuario = input('Você deseja continuar [S/N]').upper().strip()[0]
#O professor colocou a média fora do laço para o programa não fazer a conta toda vez que colocar um número
#media = soma / contador
print('Você digitou {} números e a média entre eles é de {}'.format(contador, media))
print('O MAIOR número entre eles é {} e o MENOR é {}'.format(maiorNumero, menorNumero))