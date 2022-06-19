from datetime import datetime
nasc = int(input('Digite o seu ano de NASCIMENTO, no formato (DD/MM/AA):'))
dia = datetime.today().year
idade = (dia - nasc)
if idade <= 9:
    print('Sua categoria é MIRIM, pois você tem {} ANO(s)'.format(idade))
elif idade > 9 and idade <=14:
    print('Sua categoria é INFANTIL, pois você tem {} ANOS(s)'.format(idade))
elif idade >14 and idade <= 19:
    print('Sua categoria é JUNIOR, pois vocẽ tem {} ANO(s)'.format(idade))
elif idade >19 and idade <=25:
    print('Sua categoria é SENIOR, pois você tem {} ANO(s)'.format(idade))
elif idade > 25:
    print('Sua categoria é MASTER, pois você tem {} ANOS(s)'.format(idade))



