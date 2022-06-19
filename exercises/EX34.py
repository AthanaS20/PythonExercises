salario = float(input('Digite o salário do funcionario:'))
if salario > 1250.00:
    calculo = salario * 1.1
else:
    calculo = salario * 1.15
print('O valor do seu salário com aumento é de {:.2f} R$'.format(calculo))

