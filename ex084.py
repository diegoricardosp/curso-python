pessoas = []
dados = []
pesadas = []
leves = []
cont = 0

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso (kg): ')))
    pessoas.append(dados[:])
    dados.clear()
    
