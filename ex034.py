sal = float(input('Digite seu salário: '))
if sal > 1250.00:
    a1 = sal * 0.10
    novoSal1 = a1 + sal
    print("Você receberá um aumento de 10% no valor de R${:.2f}. O novo salário será de R${:.2f}.".format(a1, novoSal1))
if sal <= 1250.00:
    a2 = sal * 0.15
    novoSal2 = a2 + sal
    print("Você receberá um aumento de 15% no valor de R${:.2f}. O novo salário será de R${:.2f}.".format(a2, novoSal2))