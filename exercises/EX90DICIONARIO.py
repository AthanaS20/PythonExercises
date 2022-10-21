aluno = {}

aluno['nome'] = input('Digite o nome:')
aluno['Média'] = float(input('Digite a média:'))


print(f'O nome do aluno é {aluno["nome"]} e a média é {aluno["Média"]}.')
if aluno["Média"] >= 6.0:
    print(f'A média foi {aluno["Média"]} e a situação é APROVADO')
elif aluno["Média"] <= 5.9:
    print(f'A média foi {aluno["Média"]} e a situação é REPROVADO')

print('FIM')



   



