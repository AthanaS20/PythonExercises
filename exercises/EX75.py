numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite mais um número:'))
numero3 = int(input('Digite outro número:'))
numero4 = int(input('Digite o último número:'))


minhaTupla = tuple([numero1, numero2, numero3, numero4])
print(f'Os valores escolhidos foram: {tuple([numero1, numero2, numero3, numero4])}')
print(f'O número 9 apareceu {(minhaTupla.count(9))} vez(s)')

if 3 in minhaTupla:
    print(f'O número 3 apareceu na {(minhaTupla.index(3))+1}º posição')
if 3 not in minhaTupla:
    print('O número 3 não foi selecionado.')

print('Os números pares são:', end='')
for pares in minhaTupla:
    if pares % 2 == 0:
        print(pares)




    
