tabela = ('Atlético - MG', 'Flamengo', 'Palmeiras', 'América - MG', 'Internacional', 'Grêmio', 'Athletico - PR', 'Santos', 'Corinthians', 'Bragantino', 'Bahia', 'Botafogo', 'Fluminense', 'Cuiabá', 'Fortaleza', 'Goiás', 'São Paulo', 'Vasco', 'Coritiba', 'Cruzeiro')

bahia = tabela.index('Bahia')+1

print(f'Tabela do brasileirão: {tabela}')

print(f'Os cinco primeiros do brasileirão são: {tabela[0:5]}')

print(f'Os últimas 4 colocado do Brasileirão 2023 são: {tabela[16:20]}')

print(f'Lista de times: {sorted(tabela)}')

print(f'O Bahia ficou na {bahia}ª posição!')
