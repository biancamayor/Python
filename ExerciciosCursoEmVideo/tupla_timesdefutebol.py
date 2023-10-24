times = ('Palmeiras','Santos','Vasco da Gama','Grêmio',
'Flamengo','Corinthians','Internacional','Cruzeiro','São Paulo','Atlético Mineiro','Botafogo',
'Fluminense','Coritiba','Bahia','Goiás','Guarani','Sport','Portuguesa','Atlético Paranaense','Vitória')

print('-='*30)
print(f'Lista de times do brasileirão: {times}')
print('-='*30)

print(f'Os 5 primeiros colocados foram: {times[:5]}') #5 primeiros
print('-='*30)

print(f'Os últimos 4 colocados foram: {times[-4:]}') #4 ultimos colocados na tabela
print('-='*30)

print(f'Os times em ordem alfabética:{sorted(times)}')
print('-='*30)