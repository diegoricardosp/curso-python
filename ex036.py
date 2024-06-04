sal = float(input("Digite o seu salário: R$"))
casa1 = float(input("Digite o valor do imóvel: R$"))
casa2 = int(input("Digite em quantos anos você pretende pagar o imóvel: "))
calc = casa1 / (casa2 * 12)
calc2 = sal * 30 / 100
if calc > calc2:
    print("Sua parcela mensal será de R${:.2f}. Ela excede o valor de 30% do seu salário, então seu empréstimo será negado.".format(calc))
elif calc2 > calc:
    print("Sua parcela mensal será de R${:.2f}. Ela não excede o valor de 30%, então seu empréstimo foi aprovado!".format(calc))