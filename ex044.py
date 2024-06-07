"""labore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
– à vista dinheiro/cheque: 10% de desconto 
– à vista no cartão: 5% de desconto 
– em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20%"""

prod = float(input("Qual o valor do produto? R$"))
cond = int(input("Qual a forma de pagamento?\n [1] À vista\n [2] Á vista no cartão\n [3] Em até 2x no cartão\n [4] Em 3x ou mais no cartão\n"))
if cond == 1:
    prod1 = prod * 0.10
    print("Você ganhou desconto de 10%. O valor do produto será de R${:.2f}.".format(prod - prod1))
elif cond == 2:
    prod2 = prod * 0.05
    print("Você ganhou desconto de 5%. O valor do produto será de R${:.2f}.".format(prod - prod2))
elif cond == 3:
    print("Você não ganhou desconto no produto. Pagará o valor normal.")
elif cond ==4:
    prod3 = prod * 0.20
    print("Nessa forma de pagamento, você pagará R${:.2f} de juros. O valor do produto será de R${:.2f}.".format(prod3, prod + prod3))
else:
    print("Opção inválida.")
