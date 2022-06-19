print('*=' * 16)
print('CALCULE AQUI SUA MÉDIA BIMESTRAL')
print('=*' * 16)
nota1 = float(input('Digite aqui a primeira nota:'))
nota2= float(input('Digite aqui a segunda nota:'))
calculo = (nota1 + nota2) / 2
if calculo > 6:
    print('Sua média é {}, portanto você foi APROVADO! Parabéns!!'.format(calculo))
elif calculo < 5:
    print('Sua média é {}, infelizmente você foi reprovado. Favor comparecer na secretaria.'.format(calculo))
elif calculo == 6 or 5.5:
    print('Sua média é {}, você está de RECUPERAÇÃO. Realize a prova para ser aprovado!'.format(calculo))
