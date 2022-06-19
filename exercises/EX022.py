nome = str(input('Digite o seu nome completo:'))
print((nome.upper()))
print(nome.lower())
print(len(nome.strip()))
divido = nome.split()
#n2 = ('-'.join(divido))
n2 = len(divido[0])

print('Seu primeiro nome tem {} letras.'.format(n2))





