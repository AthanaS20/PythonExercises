galera = ['Maria', 28],['Jorge', 15],['Lucas', 12]
print(galera[1][0]) 

#Para fazer uma lista com for
for pessoa in galera:
    print(pessoa)

#Para mostrar a idade e o nome usando for:
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

#Para receber diferentes dados:
dados = []
for cont in range(0,5):
    dados.append(input('Digite o nome:'))
    dados.append(int(input('Digite a idade:')))
    galera.append(dados[:])
    dados.clear()
print(galera)

#Para mostrar os dados especificos
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'As pessoas com mais de 21 são {pessoa[0]}')