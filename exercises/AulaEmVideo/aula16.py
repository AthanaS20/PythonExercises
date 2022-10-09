lanche = ('suco','pão','pudim', 'hamburguer')
#lanche[2] = 'Coca cola' (Esse comando não é possível, porque as tuplas são imutaveis)

print(sorted(lanche))#Para mostrar a lista ordenada (em ordem alfabetica)

for comida in lanche:
   print(f'Vou comer {comida} hoje!')

for cont in range(len(lanche)): #Também podemos a função for em range, basta mostrar a len da variavel e printar 
    print(f'Eu vou comer {lanche[cont]}')

for cont in range(len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}º') #para mostrar a posição de cada item, basta usar o cont dentro do print

for pos, comida in enumerate(lanche):
   print(f'Vou comer {comida} na posição {pos} hoje!')#para mostrar a posição de cada item, usar a função "pos(posição)" e depoos "enumarate(enumeração) na variavel"





#Podem ser executados dessas maneiras