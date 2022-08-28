print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
PrimeiroTermo = int(input('Digite o PRIMEIRO TERMO:'))
razao = int(input('Digite a RAZÃO:'))
termo = PrimeiroTermo
contador = 1
while contador <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    contador += 1
    
print('FINISH')