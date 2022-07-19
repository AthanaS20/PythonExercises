print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

termo = int(input('Digite o PRIMEIRO TERMO:'))
razao = int(input('Digite a RAZÃO:'))
calculo = termo + (10 - 1) * razao
for c in range(termo, calculo, razao):
    print('{}'.format(c), end=' -> ')
print('FINISH')


    
