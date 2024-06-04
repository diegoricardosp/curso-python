preco1 = int(input('Digite o preço do produto: '))
desc = preco1 * 0.05
preco2 = preco1 * 0.95
print('Parabéns! Você ganhou 5% de desconto. O valor do produto seria de R${:.2f}, com o desconto de R${:.2f}, ficará {:.2f}.'.format(preco1, desc, preco2))