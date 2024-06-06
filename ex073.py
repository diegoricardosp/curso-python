"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre: 
a) Os 5 primeiros times. 
b) Os últimos 4 colocados. 
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense."""

tabela = ('Atlético - MG', 'Flamengo', 'Palmeiras', 'América - MG', 'Internacional', 'Grêmio', 'Athletico - PR', 'Santos', 'Corinthians', 'Bragantino', 'Bahia', 'Botafogo', 'Fluminense', 'Cuiabá', 'Fortaleza', 'Goiás', 'São Paulo', 'Vasco', 'Coritiba', 'Cruzeiro')

bahia = tabela.index('Bahia')+1

print(f'Tabela do brasileirão: {tabela}')

print(f'Os cinco primeiros do brasileirão são: {tabela[0:5]}')

print(f'Os últimas 4 colocado do Brasileirão 2023 são: {tabela[16:20]}')

print(f'Lista de times: {sorted(tabela)}')

print(f'O Bahia ficou na {bahia}ª posição!')
