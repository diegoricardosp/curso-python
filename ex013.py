sal1 = float(input('Digite seu salário: R$'))
aumento = sal1 * 0.15
sal2 = sal1 + aumento
print('Seu salário era de R${:.2f}. Com o aumento de 15% será de R${:.2f}.'.format(sal1, sal2))