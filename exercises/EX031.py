destinoDefinidoUsuario = float(input('Digite a distancia da sua viagem em KM:'))

if destinoDefinidoUsuario <=200:
    valorDaViagem = (destinoDefinidoUsuario * 0.50)
else:
    valorDaViagem = (destinoDefinidoUsuario * 0.45)
print('O valor da sua passagem será de {:.1f} R$'.format(valorDaViagem))




