vel = int(input('Digite a velocidade que seu carro estava no dia da ocorrência:'))
if vel >80:
    print('Seu carro estava a {} KM, o mesmo foi multado.'.format(vel))
    multa = (vel - 80) * 7
    print('O valor da multa é de {} reais, clique aqui para baixar o boleto.'.format(multa))

