
times = ('Palmeiras', 'Santos','Vasco da Gama','Grêmio','Flamengo','Corinthians','Internacional','Cruzeiro','São Paulo','Atlético Mineiro','Botafogo','Fluminense','Coritiba','Bahia','Goiás','Guarani','Sport','Portuguesa','Atlético Paranaense','Vitória')

#print('-=' * 20)
#print(f'\033[1:33mLista dos times do brasileirão:\n {times}\n')
print('-=' * 20)
print('Lista de times do Brasileirão:')
for cont in range(len(times)):
    print(f'{cont} {times[cont]}')

print('-=' * 20)
print(f'\033[1:33m Os 5 primeiros times são:\n {times[0:5]} \n')

print('-=' * 20) 
print(f'\033[1:33m Os últimos 4 colocados são:\n {times[16:]} \n')

print('-=' * 20)
print(f'A lista dos times em ordem alfabética: {sorted(times)} \n')


print('-=' * 20)
print(f'São Paulo está na {times.index("São Paulo")}º posição.')
