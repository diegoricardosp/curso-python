from math import hypot
l1 = float(input("Digite o tamanho de um lado de um triângulo: "))
l2 = float(input("Digite o tamanho do outro lado do triângulo: "))
hipo = hypot(l1, l2)
print("O valor da hipotenusa desse triângulo é {:.2f}!".format(hipo))
