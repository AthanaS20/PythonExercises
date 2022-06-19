from datetime import datetime
nasc = int(input('Digite aqui o ano de nascimento com 4 DIGITOS:'))
data = datetime.today().year
idade = (data - nasc)
print('Se você nasceu em {}, sua idade é {} anos.'.format(nasc, idade))
if idade < 18:
    conta = 18 - idade
    ano = conta + data
    print('Você ainda não pode se alistar! Faltam {} ano(s) para o alistamento.'.format(conta))
    print('Seu alistamento será no ano de {}.'.format(ano))
elif idade == 18:
    print('Você pode se alistar ainda esse ANO!')
elif idade > 18:
    print('Infelizmente a idade mínima para alistamento foi atingida.')

