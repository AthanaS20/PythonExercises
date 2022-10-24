lista = [[], [], [], []]
cont = 0
soma = 0
divisão = 0
divisão = []


while True:
    nome = input('Nome:')
    lista[0].append(nome)
    nota1 = int(input('Primeira nota:'))
    lista[1].append(nota1)
    nota2 = int(input('Segunda nota:'))
    lista[2].append(nota2)
    continuar = input('Você quer continuar [S/N] ?').upper().lower()[0]
    if 'n' in continuar:
        print('=-' * 30)
        break


soma = soma + nota1 + nota2 
divisão = soma / 2
lista[3].append(divisão)



print('NOME           MÉDIA')
print('-' * 20)
print(f'{lista[0]}{[lista[3]]}' )



