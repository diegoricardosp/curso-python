"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
– EQUILÁTERO: todos os lados iguais 
– ISÓSCELES: dois lados iguais, um diferente 
– ESCALENO: todos os lados diferentes"""

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos podem formar um triângulo!")
    if r1 == r2 == r3:
        print("Formará um triângulo equilátero!")
    if r1 != r2 != r3 != r1:
        print("Formará um triângulo escaleno!")
    else:
        print("Formará um triângulo isósceles!")
else:
    print("Os segmentos não podem formar um triângulo!!")
