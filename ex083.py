lista1 = []
lista2 = []

valor = str(input('Digite uma expressão matemática: '))
priP = valor.count('(')
lista1.append(priP)
ultP = valor.count(')')
lista2.append(ultP)

if lista1 != lista2:
    print('Sua expressão está incorreta!')
else:
    print('Sua expressão está correta!')