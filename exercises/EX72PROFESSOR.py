

extensos = ('Zero', 'Um','Dois','Três','Quarto','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    numero = int(input('Digite um número de 0 a 20:'))
    if 0 <= numero <= 20:
        break
    print('Por favor, tente novamente.', end=' ')
print(f'Você escolheu o número {extensos[numero]}.')