#criei as variaveis separadas para conseguir o resultado no final
#Criei a variavel fora do laço whiletrue para contabilizar 
maiores18 = 0
sexoM = 0
sexoF = 0

while True:

    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    sexo = ' '
    seguir = ' '
    
    idade = int(input('IDADE:'))
    while sexo not in 'FM': #Se o usuario digitar uma letra inválida o programa fica repetindo até digitar o correto
        sexo = str(input('SEXO [F/M]:')).upper().strip()[0]     
    while seguir not in 'SN':
        seguir = str(input('Quer continuar?[S/N]:')).upper().strip()[0]
        
    if idade > 18:
        maiores18 += 1
    if sexo in 'Mm':
        sexoM += 1   
    if sexo in 'Ff' and idade < 20:
        sexoF =+ 1

    if seguir.lower() == 'n':
        print(f'Total de pessoas com mais de 18 anos:{maiores18}')
        print(f'Total de homens cadastrados:{sexoM}') 
        print(f'Total de mulheres com menos de 20 anos:{sexoF}')
        break
    #Quando o usuario digitar "N" parar o programa (break) e dar as estatisticas

        
        

            
        