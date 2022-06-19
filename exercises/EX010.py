real = float(input('Quanto você tem na carteira?   R$'))
dolar = real / 3.27
euro = real / 5.25
print('Com {:.2f} R$ você pode comprar {:.2f}U$! \n Com {:.2f} R$ você pode comprar  {:.2f}£! \n Obrigada por nos consultar.'.format(
    real, dolar, real, euro))
# print('Com {:.2f} reais, você pode comprar {:.2f} U$'.format(real, dolar))