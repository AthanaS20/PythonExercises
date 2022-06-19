from datetime import date
anoEscolhidoPeloUsuario = int(input('Digite um ano qualquer:'))
if anoEscolhidoPeloUsuario == 0:
    anoEscolhidoPeloUsuario = date.today().year

if anoEscolhidoPeloUsuario % 4 == 0 and anoEscolhidoPeloUsuario % 100 != 0:
        print('O Ano {} é BISSEXTO!'.format(anoEscolhidoPeloUsuario))
else:
    print('O Ano não é BISSEXTO')
