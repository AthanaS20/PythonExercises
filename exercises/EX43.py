peso = float(input('Digie aqui seu peso em KG:'))
altura = float(input('Digite aqui sua altura em M:'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('O seu IMC é de {:.2f}, você está ABAIXO do peso.'.format(imc))
elif imc > 18.5 and imc < 25:
    print('O seu IMC é de {:.2f}, você está com peso IDEAL'.format(imc))
elif imc > 20 and imc < 30:
    print('O seu IMC é de {:.2f}, você está SOBREPESO'.format(imc))
elif imc > 30 and imc < 40:
    print('O seu IMC é de {:.2f}, você está OBESO'.format(imc))
elif imc > 40:
    print('Você tem OBSIDADE MORBIDA, procure um médico.')