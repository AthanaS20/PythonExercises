from math import prod


print('*=' * 10)
print('  ' 'LOJINHA DA TATANA' '  ')
print('*=' * 10)

totalCompra = maisCaro =  maisBarato = contador = 0
barato = ''

while True:

    produto = str(input('Digite o nome do produto:'))
    preço = int(input('Digite o valor do produto:R$'))
    contador =+ 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    
    totalCompra = totalCompra + preço
    if preço >= 1000:
        maisCaro += 1
    
    if contador == 1:
        maisBarato = preço 
        
    else:
        if preço < maisBarato:
            maisBarato = preço         
             
          
    if continuar in 'Nn':
        print(f'O Total da compra foi de R${totalCompra}')
        print(f'Temos {maisCaro} produto(s) com valor acima de 1000')
        print(f'O produto mais barato foi {barato} que custa R${maisBarato:.2f}')
                   
        print('  ' 'FIM DO PROGRAMA' '    ')
        break
