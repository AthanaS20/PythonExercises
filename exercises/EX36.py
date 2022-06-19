print('\033[1;34m*' * 25)
print('\033[1;34mCALCULE AQUI O SEU ÍMOVEL\033[m')
print('\033[1;34m*\033[m' * 25)

valorCasa = float(input('Digite aqui o valor do ímovel: R$'))
salario = float(input('Digite aqui o seu sálario: R$'))
ano = int(input('Em até quantos anos deseja quitar o ímovel?'))
parcela = valorCasa / (ano * 12)
regra = salario * 30 / 100
print('Para pagar o ímovel de {:.2f} em {} anos, a prestação será de {:.3f}.'.format(valorCasa, ano, parcela))
if parcela <= regra:
    print('Seu empréstimo foi pré aprovado!')
else:
    print('Infelizmente seu empréstimo foi negado!')




