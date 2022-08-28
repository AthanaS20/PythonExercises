print('*' * 22)
print('SEQUÊNCIA DE FIBONACCI')
print('*' * 22)

numeroUsuario = int(input('Digite um número para ver sua sequência:'))
ultimoNumero = 1
penultimoNumero = 1
contador = 3
if numeroUsuario == 1:
    print('1')
elif numeroUsuario == 2:
    print('1 -> 1') 
else:
    contador = 3
    print('1 -> 1', end=' -> ')
while contador <= numeroUsuario:
    termo = ultimoNumero + penultimoNumero
    penultimoNumero = ultimoNumero
    ultimoNumero = termo
    contador += 1
    print('{}'.format(termo), end=' -> ')
print('FIM')
    


    
