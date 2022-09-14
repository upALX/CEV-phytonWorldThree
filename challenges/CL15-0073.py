# Crie uma tupla com os 20 primeiros colocados do Brasileirão, na ordem de colocação. E mostre:
# Apenas os 5 primeiros colocados. Os 4 últimos colocados. Uma lista com os times em ordem alfabetica. Em que posição na tabela está o time do Internacional.

brasilian_teams = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Atlético-PR', 'Atlético-MG', 'América-MG', 'Goiás', 'Santos', 'Bragantino', 'Botafogo', 'São Paulo', 'Ceara SC', 'Fortaleza', 'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')

# #Show 5 firsts
# for team in range(0, 5):
#     print(brasilian_teams[team])

#Show 4 lasts
print(brasilian_teams[15:20])

#Show alfa order
print(f'A tabela do Brasileirão em ordem al {sorted(brasilian_teams)}')

#Show internacional position 
print('O Internacional se encontra na posição {}'.format(brasilian_teams.index('Internacional') + 1))