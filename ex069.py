print('Cadastro de pessoas: ')
maiores = 0
h = 0
m = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]
    if sexo not in "MF": #VALIDANDO SEXO
        sexo = str(input("Dados inválidos. Informe seu sexo (M/F): ")).upper().strip()[0]
    if idade > 17:
        maiores += 1
        if sexo == 'M':
            h += 1
    elif idade < 20:
        if sexo == 'F':
            m += 1
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        print(f'Foram cadastradas {maiores} pessoas maiores de 18 anos.\n{h} são homens e {m} são mulheres menores de 20 anos.')
        break
