print('*-' * 7)
print('GERADOR DE PA V2')
print('*-' * 7)

primeiroTermo = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
contador = 1
termo = primeiroTermo
total = 0
seguir = 10

while seguir != 0:
    total += seguir
    while contador <= 10:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        contador += 1
    print('PAUSA')
    seguir = int(input('Quantos termos você quer ver a mais?'))
    contador = 1
print('FIM')


   


    




    
