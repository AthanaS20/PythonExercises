print('=' * 15)
print('LOJINHA DA TATÁ')
print('=' * 15)
compras = float(input('Digite o valor das compras (R$):'))
pagamento = int(input('Digite a forma de pagamento: \n [1] Á VISTA (DINHEIRO) OU CHEQUE (10% DESCONTO) \n [2] Á VISTA NO CARTÃO DE CRÉDITO (5% DESCONTO) \n [3] PARCELADO EM 2X \n [4] PARCELADO EM 3X  ou MAIS (20% JUROS) \n'))

if pagamento == 1:
    desconto = (10 / 100) * compras
    valor = compras - desconto 
    print('O valor das compras com desconto é R${}'.format(valor))
elif pagamento == 2:
    desconto2 = (5 / 100) * compras
    valor2 = compras - desconto2
    print('O valor da compra com desconto é R${:.2f}'.format(valor2))
elif pagamento == 3:
    valornormal = compras / 2
    print('Total da compra é R$ {:.2f}, o valor da parcela é de {:.2f}'.format(compras, valornormal))
elif pagamento == 4:
    qntparcelas = int(input('Qual a quantidade de parcelas?'))
    desconto3 = (20 / 100) * compras
    juros = desconto3 + compras
    parcela = juros / qntparcelas
    print('O valor das compras com juros é de R${:.2f}, o valor da parcela será de R${:.2f} mensais.'.format(juros, parcela))





