sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]
while sexo not in "MF":
    sexo = str(input("Dados inválidos. Informe seu sexo (M/F): ")).upper().strip()[0]
print("Registro gravado com sucesso!")

