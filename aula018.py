"""dados = ['Pedro', '25']
pessoas = []
pessoas.append(dados[:]) #sempre usar :, listra dentro de lista"""

"""pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[1][1])"""

"""teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)"""

"""galera = [['Joaquim', 13], ['Maria', 45], ['Ana', 33], ['João', 19]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')"""

galera = list()
dado = []
totmaior = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmen += 1

print(f'Temos {totmaior} maiores de idade e {totmen} menores de idade!')