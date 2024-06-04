print('----------CAIXA ELETRÔNICO----------')
while True:
    saque = int(input('Digite o valor para ser sacado: R$'))
    num1 = saque // 50
    calc1 = saque - num1 * 50
    ced50 = num1
    if ced50 > 0:
        print(f'Total de {ced50} cédulas de R$50')
    num2 = calc1 // 20
    calc2 = calc1 - num2 * 20
    ced20 = num2
    if ced20 > 0:
        print(f'Total de {ced20} cédulas de R$20')
    num3 = calc2 // 10
    calc3 = calc2 - num3 * 10
    ced10 = num3
    if ced10 > 0:
        print(f'Total de {ced10} cédulas de R$10')
    num4 = calc3 // 1
    calc4 = calc3 - num4 * 1
    ced1 = num4
    if ced1 > 0:
        print(f'Total de {ced1} cédulas de R$1')
    print(f'Obrigado por utilizar nossos serviços!')
    break
